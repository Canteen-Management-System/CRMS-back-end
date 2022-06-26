from rest_framework import viewsets

from api.serializers import CustomUserSerializer
from accounts.models import CustomUser
from rest_framework.permissions import IsAuthenticated



class CustomUserViewSet(viewsets.ModelViewSet):
   permission_classes = [IsAuthenticated]
   queryset = CustomUser.objects.all()
   serializer_class = CustomUserSerializer
