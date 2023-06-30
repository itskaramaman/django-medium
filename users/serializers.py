import bcrypt
from rest_framework import serializers
from .models import AppUser


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    username = serializers.CharField(max_length=255)
    first_name = serializers.CharField(
        max_length=255, required=False, allow_blank=True)
    last_name = serializers.CharField(
        max_length=255, required=False, allow_blank=True)
    email = serializers.EmailField()
    website = serializers.CharField(required=False, allow_blank=True)


class UserRegisterSerializer(UserSerializer):
    class Meta:
        model = AppUser

    password = serializers.CharField(max_length=255)

    def validate(self, data):
        username = data.get('username')
        email = data.get('email')

        username_exists = AppUser.objects.filter(username=username).first()
        email_exists = AppUser.objects.filter(email=email).first()

        if username_exists:
            raise serializers.ValidationError('Username already exists')

        if email_exists:
            raise serializers.ValidationError('Email already exists')

        return super().validate(data)

    def hashed_password(self, password: str):
        password_bytes = password.encode('utf-8')
        hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
        return hashed_password

    def create(self, validated_data):
        validated_data['password'] = self.hashed_password(
            validated_data['password']
        )
        return AppUser.objects.create(**validated_data)
