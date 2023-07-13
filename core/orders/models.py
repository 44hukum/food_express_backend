from django.db import models
import uuid
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from core.usermanagement.models import User
from core.product.models import Product
from django.contrib.auth.models import BaseUserManager



class OrderManager(BaseUserManager):
    def get_order_by_id(self, order_id):
        try:
           return self.get(order_id=order_id)

        except (ObjectDoesNotExist, ValueError, TypeError):
            return Http404

class Orders(models.Model):
    STATUS_CHOICES = (
        ('processing', 'proccessing'),
        ('processed', 'processed'),
        ('ready', 'ready'),
        ('on delivery', 'on delivery'),
        ('delivered', 'delivered')
    )

    PAYMENT_METHOD_CHOICES = (
        ('cash on delivery','cash on delivery'),
        ('khalti','khalti'),
        ('esewa','esewa')
    )

    PAYMENT_STATUS_CHOICES = (
        ('paid','paid'),
        ('un-paid','un-paid'),
    )

    order_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    status = models.CharField(
        max_length=100, choices=STATUS_CHOICES, default='STATUS.processing')
    payment_method = models.CharField(max_length=100, choices=PAYMENT_METHOD_CHOICES, default='cash on delivery')
    payment_status = models.CharField(max_length=100, choices=PAYMENT_STATUS_CHOICES, default='un-paid')
    created = models.DateTimeField(auto_now_add=True, help_text='Order First created')
    updated = models.DateTimeField(auto_now_add=True, help_text='Order Last updated')


    objects = OrderManager()

    class Meta:
        indexes = [
            models.Index(fields=['order_id','created', 'updated'])
        ]

    def __str__(self):
        return str(self.order_id)
    @property
    def delivery_address(self):
        return self.user.address

    @property
    def contact_number(self):
        return self.user.phonenumber


class OrderItemManager(BaseUserManager):
    def get_order_item_by_order(self, order_id):
        try:
           return self.get(order=order_id)
        except (ObjectDoesNotExist, ValueError, TypeError):
            return Http404
    def get_order_item_by_public_id(self, public_id):
        try:
            self.get(public_id=public_id)
        except (ObjectDoesNotExist, ValueError, TypeError):
            return Http404

class OrderItem(models.Model):
    public_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    item = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, help_text='Order First created')
    updated = models.DateTimeField(auto_now_add=True, help_text='Order Last updated')

    objects = OrderItemManager()

    class Meta:
        indexes = [
            models.Index(fields=['public_id','created', 'updated',])
        ]

    def __str__(self):
        return str(self.public_id)

    @property
    def item_price(self):
        return self.item.price