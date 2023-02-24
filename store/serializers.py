from rest_framework import serializers
from store.models import ItemModel, CompanyModel
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


class ItemSerializer(serializers.ModelSerializer):
    company_name = CompanySerializer()

    class Meta:
        model = ItemModel
        fields = '__all__'

    def create(self, validated_data):
        company_data = validated_data.pop('company_name')
        company = CompanyModel.objects.get_or_create(**company_data)
        item = ItemModel.objects.create(
            company_name=company[0], **validated_data)
        return item
