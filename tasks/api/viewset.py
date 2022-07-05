import email
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from tasks.models import Task, Category, ServiceType, Priority
from .serializers import TasksSerializer, CategorySerializer, PrioritySerializer, ServiceTypeSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from django.core.mail import send_mail


# Tasks View and Detail
class TasksList(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TasksSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(user=user)
    

class TaskDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TasksSerializer

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(user=user)


# Category View and Detail
class CategoryList(ListCreateAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


class CategoryDetail(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


# Priority View and Detail
class PriorityList(ListCreateAPIView):
    queryset = Priority.objects.all()
    serializer_class = PrioritySerializer
    permission_classes = [IsAuthenticated]


class PriorityDetail(RetrieveUpdateDestroyAPIView):
    queryset = Priority.objects.all()
    serializer_class = PrioritySerializer
    permission_classes = [IsAuthenticated]


# ServiceType View and Detail
class ServiceTypeList(ListCreateAPIView):
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeSerializer
    permission_classes = [IsAuthenticated]


class ServiceTypeDetail(RetrieveUpdateDestroyAPIView):
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeSerializer
    permission_classes = [IsAuthenticated]

@api_view(['GET', 'POST'])
def send_email(request):
    print(request.data)
    
    if request.method == 'POST':
        data = request.data
        send_mail(
        subject =data['subject'],
        message = data['message'],
        from_email='mohammadsalhab8@gmail.com',
        recipient_list=data['email'],
        fail_silently=False)

        return Response("recieved")


