from rest_framework import viewsets

from api.serializers import ClientSerializer
from clients.models import Client
from rest_framework.permissions import IsAuthenticated



class ClientViewSet(viewsets.ModelViewSet):
   permission_classes = [IsAuthenticated]
   queryset = Client.objects.all()
   serializer_class = ClientSerializer
