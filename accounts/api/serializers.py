from rest_framework import serializers
from accounts.models import CustomUser, Department, Role, JobTitle
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator
from phonenumber_field.modelfields import PhoneNumberField


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
            # 'employer_id'
        ]


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email',
                  'password', 'first_name', 'last_name', 'phone', 'birthday', 'position',
                  'department',
                  'role')

    first_name = serializers.CharField(required=True, max_length=32)
    last_name = serializers.CharField(required=True, max_length=32)
    birthday = serializers.DateField(required=True)
    phone = PhoneNumberField()
    position = serializers.CharField(required=True)
    department = serializers.CharField(required=True)
    role = serializers.CharField(required=True)

    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )

    username = serializers.CharField(
        required=True,
        max_length=32,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )
    password = serializers.CharField(min_length=8, write_only=True)

    def create(self, validated_data):
        first_name = validated_data.pop('first_name')
        last_name = validated_data.pop('last_name')
        phone = validated_data.pop('phone')
        birthday = validated_data.pop('birthday')
        position = validated_data.pop('position')
        department = validated_data.pop('department')
        role = validated_data.pop('role')

        user = CustomUser.objects.create_user(validated_data['username'], validated_data['email'],
                                              validated_data['password'])
        user.first_name = first_name
        user.last_name = last_name
        user.phone = phone
        user.birthday = birthday
        user.department = Department.objects.get(pk=department)
        user.position = JobTitle.objects.get(pk=position)
        user.role = Role.objects.get(pk=role)
        user.save()
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
