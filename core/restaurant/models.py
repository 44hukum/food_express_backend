from django.db import models
import uuid
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
import os
from functools import partial

class RestaurantManager(models.Manager):
    def get_object_by_public_id(self, public_id):
        try:
            return self.get(public_id=public_id)
        except (ObjectDoesNotExist, ValueError, TypeError):
            return Http404
        

class Restaurant(models.Model):
    def update_filename(self, filename, path):
        path = path
        filename = 'logo_{0}'.format(self.public_id)
        return os.path.join(path,filename)
    

    STATUS = (
        ('open','open'),
        ('closed','closed'),

    )
    public_id = models.UUIDField(unique=True, default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=128)
    delivery_fee = models.CharField(max_length=3)
    contact_number = models.CharField(max_length=13)
    status = models.CharField(max_length=30, choices=STATUS, default='open')
    delivery_time = models.CharField(max_length=100, default="10:00 AM - 9:00 PM")
    email = models.EmailField()
    logo = models.ImageField(upload_to='restaurants', default='default/restautant.png')


    created = models.DateTimeField(auto_now_add=True, help_text='First Created')
    updated = models.DateTimeField(auto_now=True, help_text='Last Updated')

    objects = RestaurantManager()

    class Meta:
        indexes = [
            models.Index(fields=['name', 'public_id','created', 'updated'])
        ]

    def __str__(self):
        return str(self.name)


class BusinessHours(models.Model):
    public_id = models.UUIDField(unique=True, default=uuid.uuid4, primary_key=True, editable=False)

    created = models.DateTimeField(auto_now_add=True, help_text='First Created')
    updated = models.DateTimeField(auto_now=True, help_text='Last Updated')

    class Meta:
        indexes = [
            models.Index(fields=['public_id','created', 'updated'])
        ]

    def __str__(self):
        return str(self.name)