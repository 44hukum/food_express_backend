from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets
from core.product.models import Product
from core.product.seralizers import ProductSeralizer
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import filters, generics

class ProductViewSets(viewsets.ModelViewSet):
    http_method_names = ('post', 'get', 'put', 'delete')
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ProductSeralizer
    parser_classes = (FormParser, MultiPartParser)

    def get_queryset(self):
        return Product.objects.all()
    
    def get_object(self):
        return Product.objects.get_product_by_public_id(self.kwargs['pk'])
    
class ProductSearchViewsets(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSeralizer
    filter_backends = [filters.SearchFilter]
    # permission_classes = [IsAuthenticated]
    search_fields = ['product_name', 'category__category_name', 'description']