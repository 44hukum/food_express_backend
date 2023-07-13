from rest_framework import serializers
from core.orders.models import Orders, OrderItem


class OrderItemsSeralizer(serializers.ModelSerializer):
    price = serializers.CharField(max_length=10, required=False, read_only=True)
    class Meta:
        model = OrderItem
        fields = ['public_id','item','quantity','price','created','updated']

class OrdersSeralizer(serializers.ModelSerializer):
    status = serializers.CharField(max_length=100, read_only=True, required=False)
    payment_status = serializers.CharField(max_length=100, read_only=True, required=False)

    order_items = OrderItemsSeralizer(many=True)
    class Meta:
        model = Orders
        fields = ['order_id','user','status','payment_method','payment_status','updated','created','order_items']

    def create(self, validated_data):
        order_item_data = validated_data.pop('order_items')
        order = Orders.objects.create(**validated_data)
        for i in order_item_data:
            OrderItem.objects.create(order=order,**i)
        
        orderItems = OrderItem.objects.filter(order=order)
        order_item_list = [{
            'public_id': items.public_id,
            'item': items.item,
            'quantity': items.quantity,
            'price': items.item_price
        } for items in orderItems]

        return_dict = {
            'order_id': order.order_id,
            'user': order.user,
            'status': order.status,
            'payment_method': order.payment_method,
            'payment_status': order.payment_status,
            'order_items': order_item_list,
            'created': order.created,
            'updated': order.updated
        }
        return return_dict

class OrdersUserSeralizer(serializers.ModelSerializer):
    status = serializers.CharField(max_length=100, read_only=True, required=False)
    order_items = OrderItemsSeralizer(many=True)
    class Meta:
        model = Orders
        fields = ['order_id','user','status','updated','created','order_items']