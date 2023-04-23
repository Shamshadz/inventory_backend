from rest_framework import serializers
from store.models import (ItemModel, VCompanyModel, CompanyModel, VehicleModel,
                           DashBoardModel, LocationModel, DelayTranscation)
from django.db import IntegrityError


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyModel
        fields = '__all__'

    def create(self, validated_data):
        try:
            company = CompanyModel.objects.create(
                company_name=validated_data['company_name'],
            )
            company.save()
            return company
        except IntegrityError as e:
            raise serializers.ValidationError({
                "errors": str(e)
            })
        
class VCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = VCompanyModel
        fields = '__all__'

    def create(self, validated_data):
        try:
            vcompany = VCompanyModel.objects.create(
                vcompany_name=validated_data['vcompany_name'],
            )
            vcompany.save()
            return vcompany
        except IntegrityError as e:
            raise serializers.ValidationError({
                "errors": str(e)
            })

class VehicleSerializer(serializers.ModelSerializer):
    vcompany = VCompanySerializer()

    class Meta:
        model = VehicleModel
        fields = '__all__'

    def create(self, validated_data):
        vcompany_data = validated_data.pop('vcompany')
        vehicle_name_data = validated_data.pop('vehicle_name')

        vcompany = VCompanyModel.objects.get_or_create(**vcompany_data)
        vehicle = VehicleModel.objects.get_or_create(
            vcompany=vcompany[0], vehicle_name=vehicle_name_data, **validated_data)

        return vehicle[0]

class ItemSerializer(serializers.ModelSerializer):
    company_name = CompanySerializer()
    vehicle_name = VehicleSerializer()

    class Meta:
        model = ItemModel
        fields = '__all__'

    def create(self, validated_data):
        company_data = validated_data.pop('company_name')
        vehicle_data = validated_data.pop('vehicle_name')

        company = CompanyModel.objects.get_or_create(**company_data)
        vcompany = VCompanyModel.objects.get_or_create(vcompany_name =vehicle_data['vcompany']['vcompany_name'])
        vehicle = VehicleModel.objects.get_or_create(
            vcompany =vcompany[0], vehicle_name =vehicle_data['vehicle_name'], wheeler=vehicle_data['wheeler'])
        
        item = ItemModel.objects.create(
            company_name=company[0], vehicle_name =vehicle[0] , **validated_data)
        return item
    
    def update(self, instance, validated_data):
        company_name_data = validated_data.pop('company_name', None)
        vehicle_name_data = validated_data.pop('vehicle_name', None)

        for key, value in validated_data.items():
            setattr(instance, key, value)
        
        # company_name_pk = company_name_data.get('id', None) if company_name_data else None
        company_name_instance = None

        try:
            company_name_pk = CompanyModel.objects.get(**company_name_data).id
        except:
            new_company_name = CompanyModel.objects.get_or_create(**company_name_data)
            new_company_name = new_company_name[0]
            company_name_pk = CompanyModel.objects.get(**company_name_data).id
            

        if company_name_pk:
            company_name_queryset = CompanyModel.objects.filter(pk=company_name_pk)
            if company_name_queryset.exists():
                company_name_instance = company_name_queryset.first() # or vehicle_name_queryset[0]

        instance.company_name = company_name_instance

        # vehicle_name_pk = vehicle_name_data.get('id', None) if vehicle_name_data else None
        vehicle_name_instance = None
        

        new_vcompany = VCompanyModel.objects.get_or_create(vcompany_name =vehicle_name_data['vcompany']['vcompany_name'])
        new_vehicle_name = VehicleModel.objects.get_or_create(vcompany =new_vcompany[0], 
                                                        vehicle_name =vehicle_name_data['vehicle_name'], wheeler=vehicle_name_data['wheeler'])
        
        new_vehicle_name = new_vehicle_name[0]
        vehicle_name_pk = VehicleModel.objects.get(vehicle_name =vehicle_name_data['vehicle_name'], wheeler=vehicle_name_data['wheeler']).id


        if vehicle_name_pk:
            vehicle_name_queryset = VehicleModel.objects.filter(pk=vehicle_name_pk)
            if vehicle_name_queryset.exists():
                vehicle_name_instance = vehicle_name_queryset.first()  # or vehicle_name_queryset[0]

        instance.vehicle_name = vehicle_name_instance

        instance.save()
        return instance
    


class DashBoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = DashBoardModel
        fields = '__all__'


    def create(self, validated_data):
        try:
            dashBoard = DashBoardModel.objects.create(
                **validated_data
            )
            dashBoard.save()
            return dashBoard
        except IntegrityError as e:
            raise serializers.ValidationError({
                "errors": str(e)
            })
    
class LoacationSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()
    
    class Meta:
        model = LocationModel
        fields = ['id', 'location' , 'photo', 'photo_url']

    def get_photo_url(self, obj):
        request = self.context.get('request')
        if obj.photo:
            photo_url = obj.photo.url
            if request is not None:
                photo_url = request.build_absolute_uri(photo_url)
            return photo_url
        else:
            return None

    def create(self, validated_data):
        my_instance = LocationModel.objects.create(
            photo=validated_data.get('photo'),
            location=validated_data.get('location'),
        )
        return my_instance

class QNotifierSerializer(serializers.ModelSerializer):
    vehicle_name = VehicleSerializer()

    class Meta:
        model = ItemModel
        fields = ['id', 'quantity', 'quantity_limit', 'description', 'vehicle_name']

class DelayTranscationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DelayTranscation
        fields = '__all__'

#### Medical Serializers
######################################################################################
from store.models import (MedicineModel, MedLocationModel, MedDashBoardModel)

class MedicineSerializer(serializers.ModelSerializer):

    class Meta:
        model = MedicineModel
        fields = '__all__'

    def create(self, validated_data):
        try:
            medicine = MedicineModel.objects.create(
               **validated_data
            )
            medicine.save()
            return medicine
        except IntegrityError as e:
            raise serializers.ValidationError({
                "errors": str(e)
            })
    
    def update(self, instance, validated_data):

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance
    


class MedDashBoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = MedDashBoardModel
        fields = '__all__'


    def create(self, validated_data):
        try:
            dashBoard = MedDashBoardModel.objects.create(
                **validated_data
            )
            dashBoard.save()
            return dashBoard
        except IntegrityError as e:
            raise serializers.ValidationError({
                "errors": str(e)
            })
    
class MedLoacationSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()
    
    class Meta:
        model = MedLocationModel
        fields = ['id', 'location' , 'photo', 'photo_url']

    def get_photo_url(self, obj):
        request = self.context.get('request')
        if obj.photo:
            photo_url = obj.photo.url
            if request is not None:
                photo_url = request.build_absolute_uri(photo_url)
            return photo_url
        else:
            return None

    def create(self, validated_data):
        my_instance = MedLocationModel.objects.create(
            photo=validated_data.get('photo'),
            location=validated_data.get('location'),
        )
        return my_instance

class MQNotifierSerializer(serializers.ModelSerializer):

    class Meta:
        model = MedicineModel
        fields = ['id', 'name', 'quantity','description']