from rest_framework import serializers
from stores.models import *


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class DepartmentSerializer(serializers.ModelSerializer):
    location_name = serializers.CharField(source='location.location', read_only=True)

    class Meta:
        model = Department
        fields = ('id', 'name', 'location', 'location_name')


class SubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = SubCategory
        fields = ('id', 'subcategory')


class CategorySerializer(serializers.ModelSerializer):
    location_name = serializers.CharField(source='department.location.location', read_only=True)
    department_name = serializers.CharField(source='department.name', read_only=True)
    subcategories = serializers.ListSerializer(child=SubCategorySerializer(), source='subcategory_set', read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'department', 'location_name', 'department_name', 'category', 'subcategories')