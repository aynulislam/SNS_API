from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import ScUser,ScLoginHistory


class CustomJWTSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        credentials = {
            'username': '',
            'password': attrs.get("password")
        }
        user_obj = User.objects.filter(email=attrs.get("username")).first() or User.objects.filter(username=attrs.get("username")).first()
        if user_obj:
            credentials['username'] = user_obj.username
        return super().validate(credentials)


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(max_length=32, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(min_length=8, write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        if self.user.is_superuser:
            data['role']='superuser'
        elif self.user.is_staff:
            data['role'] = 'admin'
        else:
            data['role'] = 'user'
        data['username'] = self.user.username
        data['email'] = self.user.email
        return data


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScUser
        fields = '__all__'


class UserLoginHistorySerialize(serializers.ModelSerializer):
    class Meta:
        model = ScLoginHistory
        fields = '__all__'
