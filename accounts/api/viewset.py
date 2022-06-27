from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView 

from .serializers import CustomUserSerializer
from accounts.models import CustomUser
from rest_framework.permissions import IsAuthenticated



class CustomUserViewSet(ListCreateAPIView):
   permission_classes = [IsAuthenticated]
   queryset = CustomUser.objects.all()
   serializer_class = CustomUserSerializer
