from rest_framework import serializers
from apps.users.models import User
from django.contrib.auth.hashers import make_password
import secrets

class UserTokenSerializer( serializers.ModelSerializer ):

    class Meta:

        model = User
        fields = '__all__'


class UserByAdminSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:

        model = User
        fields = ('email', 'password', 'created_by','name','is_active')

    def validate_password(self, value):
        return make_password(value)



class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = '__all__'


    def create(self, validated_data):

        user = User(**validated_data)
        user.set_password( validated_data['password'] )
        if(validated_data['is_admin']):
            user.is_admin = True
        user.api_token_email = secrets.token_hex(16)
        user.save()

        return user 
    
    def update(self, instance, validated_data):

        updated_user = super().update(instance, validated_data)
        updated_user.set_password( validated_data['password'] )
        updated_user.save()
        return updated_user


class UserListSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

    def to_representation(self, instance):

        return {
            'id' : instance['id'],
            'username' : instance['username'],
            'email' : instance['email'],
            'password' : instance['password']
        }
    


class PasswordChangeSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    new_password1 = serializers.CharField(required=True)
    new_password2 = serializers.CharField(required=True)

    def validate(self, attrs):
        if attrs['new_password1'] != attrs['new_password2']:
            raise serializers.ValidationError({"new_password2": "Las contraseñas no coinciden."})
        
        return attrs