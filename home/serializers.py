from rest_framework import serializers
from home.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['email', 'name', 'tc', 'password', "password2"]
        extra_kwargs = {
            'password': {'write_only': True},
            'password2': {'write_only': True},
        }
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.pop('password2')
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})    
        return super().validate(attrs)    

    def create(self, validated_data):
        user = User.objects.create_user(
            **validated_data
        )
        return user
    



class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    # password = serializers.CharField(max_length=68, min_length=6, write_only=True)  
    class Meta:
        model = User
        fields = ['email', 'password']
