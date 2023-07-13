from rest_framework import serializers
from core.restaurant.models import Restaurant, BusinessHours

class RestaurantSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

class BusinessHourSeralizer(serializers.ModelSerializer):
    class Meta:
        model = BusinessHours
        fields = '__all__'