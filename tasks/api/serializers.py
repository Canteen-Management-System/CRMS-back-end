from rest_framework import serializers
from tasks.models import Task, Category, Priority, ServiceType


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Task


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Category


class PrioritySerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Priority


class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = ServiceType
