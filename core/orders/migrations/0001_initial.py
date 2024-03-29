# Generated by Django 4.1.7 on 2023-07-12 08:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core_product', '0003_product_category'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('public_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Order First created')),
                ('updated', models.DateTimeField(auto_now_add=True, help_text='Order Last updated')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core_product.product')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('processing', 'proccessing'), ('processed', 'processed'), ('ready', 'ready'), ('on delivery', 'on delivery'), ('delivered', 'delivered')], default='STATUS.processing', max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Order First created')),
                ('updated', models.DateTimeField(auto_now_add=True, help_text='Order Last updated')),
                ('order_items', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core_orders.orderitem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddIndex(
            model_name='orders',
            index=models.Index(fields=['order_id', 'created', 'updated'], name='core_orders_order_i_8d447b_idx'),
        ),
        migrations.AddIndex(
            model_name='orderitem',
            index=models.Index(fields=['public_id', 'created', 'updated'], name='core_orders_public__3ba3e7_idx'),
        ),
    ]
