from rest_framework import serializers
from store.models import ItemModel, CompanyModel, VehicleModel
from django.db import IntegrityError
from rest_framework.serializers import PrimaryKeyRelatedField


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

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleModel
        fields = '__all__'

    def create(self, validated_data):
        try:
            vehicle = VehicleModel.objects.create(
                vehicle_name=validated_data['vehicle_name'],
            )
            vehicle.save()
            return vehicle
        except IntegrityError as e:
            raise serializers.ValidationError({
                "errors": str(e)
            })

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
        vehicle = VehicleModel.objects.get_or_create(**vehicle_data)
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

        try:
            vehicle_name_pk = VehicleModel.objects.get(**vehicle_name_data).id
        except:
            new_vehicle_name = VehicleModel.objects.get_or_create(**vehicle_name_data)
            new_vehicle_name = new_vehicle_name[0]
            vehicle_name_pk = VehicleModel.objects.get(**vehicle_name_data).id

        if vehicle_name_pk:
            vehicle_name_queryset = VehicleModel.objects.filter(pk=vehicle_name_pk)
            if vehicle_name_queryset.exists():
                vehicle_name_instance = vehicle_name_queryset.first()  # or vehicle_name_queryset[0]

        # if vehicle_name_instance is None and vehicle_name_data:
        #     vehicle_name_serializer = VehicleSerializer(instance.vehicle_name, data=vehicle_name_data)
        #     if vehicle_name_serializer.is_valid():
        #         vehicle_name_instance = vehicle_name_serializer.save()
        #     else:
        #         raise serializers.ValidationError(vehicle_name_serializer.errors)

        instance.vehicle_name = vehicle_name_instance

        instance.save()
        return instance
    