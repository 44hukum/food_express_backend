from rest_framework import serializers
from core.product.models import Product

class ProductSeralizer(serializers.ModelSerializer):
    category_name = serializers.CharField(max_length=100)
    image = serializers.ImageField(required=True)
    class Meta:
        model = Product
        fields = '__all__'