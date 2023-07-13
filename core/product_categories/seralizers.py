from rest_framework.permissions import AllowAny
from rest_framework import serializers
from core.product_categories.models import ProductCategories

class ProductCategoriesSeralizers(serializers.ModelSerializer):
    class Meta:
        model = ProductCategories
        fields = '__all__'