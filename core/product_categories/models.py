from django.db import models
import uuid 
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

class ProductCategoriesManager(models.Manager):
    def get_product_category_by_public_id(self, public_id):
        try:
            return self.get(public_id=public_id)
        except (ObjectDoesNotExist, ValueError, TypeError):
            return Http404
        

class ProductCategories(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    category_name = models.CharField(max_length=32)

    created = models.DateTimeField(auto_now_add=True, help_text='Product category created at')
    updated = models.DateTimeField(auto_now=True, help_text='Product category last updated')

    objects = ProductCategoriesManager()

    class Meta:
        indexes = [
            models.Index(fields=['public_id', 'category_name', 'created', 'updated'])
        ]

    def __str__(self):
        return str(self.category_name)
