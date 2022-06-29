from statistics import mode
from rest_framework import serializers
from accounts.models import CustomUser, Department, Role, JobTitle
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['role'] = str(user.role)
        token['first_name'] = user.first_name
        token['position'] = str(user.position)
        token['department'] = str(user.department)
        token['email'] = str(user.email)

        return token

class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = [
            'id',
            'first_name',
            'last_name',
            'position',
            'phone',
            'birthday',
            'department',
            'role',
            'email',
        ]

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password')
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=CustomUser.objects.all())]
            )
    username = serializers.CharField(
            required = True,
            max_length=32,
            validators=[UniqueValidator(queryset=CustomUser.objects.all())]
            )
    password = serializers.CharField(min_length=8,write_only=True)

    def create(self, validated_data):
        user = CustomUser.objects.create_user(validated_data['username'], validated_data['email'],
             validated_data['password'])
        return user

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"


class JobTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobTitle
        fields = "__all__"
