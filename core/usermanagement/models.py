import uuid
from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.http import Http404


class UserManager(BaseUserManager):
    def get_object_by_public_id(self, public_id):
        try:
            return self.get(public_id=public_id)
        except (ObjectDoesNotExist, ValueError, TypeError):
            return Http404

    def create_user(self, username, email, password=None, **kwargs):
        """ Create User"""    
        if username is None:
            raise TypeError('Username is required')
        if email is None:
            raise TypeError('Email is required')
        if password is None:
            raise TypeError('Password is required')

        user = self.model(username=username, email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, username, email, phonenumber, password=None, **kwargs):
        """ Create super user"""
        if username is None:
            raise TypeError('Username is required')
        if email is None:
            raise TypeError('Email is required')
        if password is None:
            raise TypeError('Users must have an password')
        if phonenumber is None:
            raise TypeError('Users must have an contact number')

        user = self.create_user(username=username, email=email, password=password, phonenumber=phonenumber, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    public_id = models.UUIDField(db_index=True, unique=True, default=uuid.uuid4, editable=False) # User_id
    username = models.CharField(db_index=True, max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(db_index=True, unique=True)
    phonenumber = models.CharField(db_index=True,max_length=15,unique=True)
    address = models.CharField(db_index=True, max_length=50, default='kathmandu,')
    is_active = models.BooleanField(default=True)
    
    is_staff = models.BooleanField(default=False)

    is_superuser = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now=True) # Time stamp when the user is created
    updated = models.DateTimeField(auto_now_add=True) # Timestamp when the user is updated

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phonenumber']

    objects = UserManager()

    @property
    def name(self): # __str__
        return f" {self.first_name} {self.last_name}"
    
