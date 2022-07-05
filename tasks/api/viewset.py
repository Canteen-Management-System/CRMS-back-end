from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from tasks.models import Task, Category, ServiceType, Priority, ClientReq
from .serializers import TasksSerializer, CategorySerializer, PrioritySerializer, ServiceTypeSerializer, ClientReqSerializer
from rest_framework.permissions import IsAuthenticated


class TasksList(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TasksSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        if user.role.name == 'Staff':
            return Task.objects.all()
        return Task.objects.filter(user=user)


class TaskDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TasksSerializer

    # def get_queryset(self):
    #     user = self.request.user
    #     return Task.objects.filter(user=user)


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


# ClientRequest View and Detail
class ClientReqList(ListCreateAPIView):
    queryset = ClientReq.objects.all()
    serializer_class = ClientReqSerializer
    permission_classes = []


class ClientReqDetail(RetrieveUpdateDestroyAPIView):
    queryset = ClientReq.objects.all()
    serializer_class = ClientReqSerializer
    permission_classes = []
