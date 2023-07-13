from rest_framework import serializers
from core.usermanagement.serializers import UserSerializer
from core.usermanagement.models import User

class RegisterSerializer(UserSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True) # Make sure password is 8 character

    class Meta:
        model = User
        fields = ['id', 'public_id', 'email', 'username', 'first_name', 'last_name', 'phonenumber', 'password','address']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    