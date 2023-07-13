from django.contrib import admin
from core.orders.models import OrderItem, Orders


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    raw_id_fields = ['order']


@admin.register(Orders)
class OrderAdmin(admin.ModelAdmin):
    list_display= [
        'user','status','order_id','created','updated', 'payment_status', 'payment_method', 'contact_number','delivery_address'
    ]
    list_editable=['status', 'payment_status']
    inlines = [OrderItemInline]