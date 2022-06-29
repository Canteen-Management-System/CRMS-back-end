from statistics import mode
from rest_framework import serializers
from accounts.models import CustomUser, Department, Role, JobTitle
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


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
