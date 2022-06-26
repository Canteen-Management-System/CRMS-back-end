from rest_framework import serializers

from accounts.models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
   class Meta:
       model = CustomUser
       fields = ['first_name',
                 'lastName',
                 'position',
                 'phone',
                 'birthday',
                 'department',
                 'role,',
                 'email',
                 'staff',
                 'admin',
                 'active'
                ]

