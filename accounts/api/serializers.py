from rest_framework import serializers

from accounts.models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
   class Meta:
       model = CustomUser
       fields = ['employer_id',
                 'first_name',
                 'last_name',
                 'position',
                 'phone',
                 'birthday',
                 'department',
                 'role',
                 'email',
                 'staff',
                 'admin',
                 'active'
                ]

