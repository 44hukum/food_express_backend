from django.db import models
import uuid
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from core.product_categories.models import ProductCategories

class ProductManager(models.Manager):
    def get_product_by_public_id(self, public_id):
        try:
            return self.get(public_id=public_id)
        except (ObjectDoesNotExist, ValueError, TypeError):
            return Http404


class Product(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    product_name = models.CharField(max_length=128)
    price = models.CharField(max_length=4)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products')
    category = models.ForeignKey(ProductCategories, on_delete=models.DO_NOTHING, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True, help_text='Product created')
    updated = models.DateTimeField(auto_now=True, help_text='Product Last updated')

    objects = ProductManager()
    
    class Meta:
        indexes = [
            models.Index(fields=['public_id', 'product_name', 'created', 'updated'])
        ]
    @property
    def category_name(self):
        return str(self.category.category_name)

    def __str__(self):
        return str(self.product_name)