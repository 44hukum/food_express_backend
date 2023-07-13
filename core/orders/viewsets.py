from core.orders.models import Orders, OrderItem
from core.orders.seralizers import OrdersSeralizer, OrdersUserSeralizer
from rest_framework.parsers import FormParser, MultiPartParser

from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

class OrdersViewsets(viewsets.ModelViewSet):
    http_method_names = ('post', 'get', 'put', 'delete')
    permission_classes =(AllowAny,)
    serializer_class = OrdersSeralizer
    
    def get_queryset(self):
        orders = Orders.objects.all()
        return_list = []
        for order in orders:
            return_dict = {
                'order_id': order.order_id,
                'user': order.user,
                'status': order.status, 
                'order_items': OrderItem.objects.filter(order=order),
                'created': order.created,
                'updated': order.updated
            }
            return_list.append(return_dict)
        return return_list
    
    def get_object(self):
        order = Orders.objects.get_order_by_id(self.kwargs['pk'])
        return_dict = {
            'order_id': order.order_id,
            'user': order.user,
            'status': order.status, 
            'order_items': OrderItem.objects.filter(order=order),
            'created': order.created,
            'updated': order.updated
        }
        return return_dict

class UserOrderViewsets(viewsets.ModelViewSet):
    http_method_names = ('get',)
    permission_classes = (AllowAny,)
    serializer_class = OrdersUserSeralizer
    parser_classes = (FormParser,)

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        context = self.get_serializer_context()
        context['user_id'] = self.request.query_params.get('user_id')
        kwargs['context'] = context
        return serializer_class(*args, **kwargs)

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter(
            'user_id',
            openapi.IN_QUERY,
            description='User ID',
            type=openapi.TYPE_STRING
        )
    ])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        orders = Orders.objects.filter(user_id=user_id)
        order = Orders.objects.get_order_by_id(self.kwargs['pk'])

        return_list = []
        for order in orders:
            return_dict = {
                'order_id': order.order_id,
                'user': order.user,
                'status': order.status, 
                'order_items': OrderItem.objects.filter(order=order),
                'created': order.created,
                'updated': order.updated
            }
            return_list.append(return_dict)
        return return_list

    def get_object(self):
        user_id = self.request.query_params.get('user_id')
        order = Orders.objects.filter(user_id=user_id)
        return_dict = {
            'order_id': order.order_id,
            'user': order.user,
            'status': order.status, 
            'order_items': OrderItem.objects.filter(order=order),
            'created': order.created,
            'updated': order.updated
        }
        return return_dict