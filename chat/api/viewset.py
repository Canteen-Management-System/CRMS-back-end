from typing_extensions import Self
from rest_framework import generics, serializers
from accounts.models import CustomUser
from chat.models import Chat
from rest_framework.permissions import IsAuthenticated

from .serializers import ChatSerializer
# from accounts.api.serializers import CustomUserSerializer

# class CustomUserList(generics.ListCreateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer

#     def get_queryset(self):

#         queryset = CustomUser.objects.all()
#         return queryset

class ChatList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    
    serializer_class = ChatSerializer

    def get_queryset(self):
      queryset = Chat.objects.all()
      from_id = self.request.query_params.get('from_id')
      to_id = self.request.query_params.get('to_id')
      queryset1 = Chat.objects.filter(from_id=from_id,to_id=to_id)
      queryset2 = Chat.objects.filter(from_id=to_id,to_id=from_id)
      queryset =  queryset1.union(queryset2)
      
      return queryset