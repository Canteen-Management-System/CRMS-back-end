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


# ['__class__', '__class_getitem__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__slotnames__', '__str__', '__subclasshook__', '__weakref__', '_constructor_args', '_db', '_get_queryset_methods', '_hints', '_insert', '_queryset_class', '_set_creation_counter', '_update', 'aggregate', 'alias', 'all', 'annotate', 'auto_created', 'bulk_create', 'bulk_update', 'check', 'complex_filter', 'contains', 'contribute_to_class', 'count', 'create', 'creation_counter', 'dates', 'datetimes', 'db', 'db_manager', 'deconstruct', 'defer', 'difference', 'distinct', 'earliest', 'exclude', 'exists', 'explain', 'extra', 'filter', 'first', 'from_queryset', 'get', 'get_or_create', 'get_queryset', 'in_bulk', 'intersection', 'iterator', 'last', 'latest', 'model', 'name', 'none', 'only', 'order_by', 'prefetch_related', 'raw', 'reverse', 'select_for_update', 'select_related', 'union', 'update', 'update_or_create', 'use_in_migrations', 'using', 'values', 'values_list']

# ['DoesNotExist', 'MultipleObjectsReturned', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_check_column_name_clashes', '_check_constraints', '_check_default_pk', '_check_field_name_clashes', '_check_fields', '_check_id_field', '_check_index_together', '_check_indexes', '_check_local_fields', '_check_long_column_names', '_check_m2m_through_same_relationship', '_check_managers', '_check_model', '_check_model_name_db_lookup_clashes', '_check_ordering', '_check_property_name_related_field_accessor_clashes', '_check_single_primary_key', '_check_swappable', '_check_unique_together', '_do_insert', '_do_update', '_get_FIELD_display', '_get_expr_references', '_get_next_or_previous_by_FIELD', '_get_next_or_previous_in_order', '_get_pk_val', '_get_unique_checks', '_meta', '_perform_date_checks', '_perform_unique_checks', '_prepare_related_fields_for_save', '_save_parents', '_save_table', '_set_pk_val', 'check', 'clean', 'clean_fields', 'customuser_set', 'date_error_message', 'delete', 'from_db', 'full_clean', 'get_deferred_fields', 'id', 'jobtitle_set', 'name', 'objects', 'pk', 'prepare_database_save', 'refresh_from_db', 'save', 'save_base', 'serializable_value', 'task_set', 'unique_error_message', 'validate_unique']
