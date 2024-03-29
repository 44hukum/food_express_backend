from django.contrib import admin
from core.product.models import Product

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','price', 'category_name')