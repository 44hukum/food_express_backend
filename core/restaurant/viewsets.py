from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from core.restaurant.seralizers import RestaurantSeralizer, BusinessHourSeralizer
from core.restaurant.models import Restaurant, BusinessHours

class RestaurantViewSets(viewsets.ModelViewSet):
    http_method_names = ('post', 'get', 'put', 'delete')
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = RestaurantSeralizer

    def get_queryset(self):
        return Restaurant.objects.all()
    
    def get_object(self):
        return Restaurant.objects.get_object_by_public_id(self.kwargs['pk'])


class BusinessHourViewSets(viewsets.ModelViewSet):
    http_method_names = ('post', 'get', 'put', 'delete')
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = BusinessHourSeralizer

    def get_queryset(self):
        return BusinessHours.objects.all()