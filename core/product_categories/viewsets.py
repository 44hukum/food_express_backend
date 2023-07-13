from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets
from core.product_categories.models import ProductCategories
from core.product_categories.seralizers import ProductCategoriesSeralizers

class ProductCategoriesViewsets(viewsets.ModelViewSet):
    http_method_names = ('post', 'get', 'put', 'delete')
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ProductCategoriesSeralizers

    def get_queryset(self):
        return ProductCategories.objects.all()
    
    def get_object(self):
        return ProductCategories.objects.get_product_category_by_public_id(self.kwargs['pk'])