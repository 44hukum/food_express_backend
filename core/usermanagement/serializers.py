from rest_framework import serializers
from core.usermanagement.models import User

class UserSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'public_id', 'username', 'first_name','phonenumber', 'address', 'last_name', 'email', 'is_active', 'created', 'updated']
        read_only_field = ['is_active']