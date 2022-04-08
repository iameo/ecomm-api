from jsonschema import ValidationError
from rest_framework import serializers
from .models import ProductManager, ProductBuyer, CustomUser
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator


class CustomerRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'password2', 'first_name', 'last_name', 'dob')
        extra_kwargs = {
            'first_name': {'required':True},
            'last_name': {'required':True},
            'dob': {'required': True}
        } 
        

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError("Passwords do not match")
        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create(
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name']
        )
        user.is_productBuyer = True
        user.set_password(validated_data['password'])
        user.save()
        customer = ProductBuyer.objects.get_or_create(acc_type=user)
        print(customer)
        # customer.save()
        return customer




