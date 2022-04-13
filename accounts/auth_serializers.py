from rest_framework import serializers
from .models import CustomUser, SellerRating
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.permissions import AllowAny

from utils import calculate_age



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """TOKEN-Tolkien"""
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['name'] = user.full_name
        return token


    
class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'confirm_password', 'first_name', 'last_name', 'date_of_birth']
        extra_kwargs = {
            'first_name': {'required':True},
            'last_name': {'required':True},
            'date_of_birth': {'required': True}
        } 
        

    def validate(self, attrs):
        age = calculate_age(attrs['date_of_birth'])

        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError("Passwords do not match")
        if age < 18:
            raise serializers.ValidationError("User must be at least 18 years old")
        return attrs
    
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.location = validated_data.get('location', instance.location)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.save()
        return instance
  

class CustomerRegistrationSerializer(RegistrationSerializer):
    def create(self, validated_data):
        user = create_custom_user(True, False, validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class SellerRegistrationSerializer(RegistrationSerializer):
    def create(self, validated_data):
        user = create_custom_user(False, True, validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user



def create_custom_user(customer: bool, seller: bool, data: dict) -> CustomUser:
    user = CustomUser.objects.create(
        email = data['email'],
        first_name = data['first_name'],
        last_name = data['last_name'],
        date_of_birth = data['date_of_birth'],
        is_productManager = seller,
        is_productBuyer = customer
)
    return user
