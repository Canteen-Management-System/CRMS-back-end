from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView 
from .serializers import ClientSerializer
from clients.models import Client
from rest_framework.permissions import IsAuthenticated



class ClientViewSet(ListCreateAPIView):
   permission_classes = [IsAuthenticated]
   queryset = Client.objects.all()
   serializer_class = ClientSerializer
