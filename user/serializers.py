from dataclasses import field, fields
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    id =serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields =(
            'id', 'email','first_name','last_name', 'last_name',
           'is_staff','is_active','is_superuser','password'
        )
    def create(self, validated_data):
        user= super(UserSerializer,self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return User

