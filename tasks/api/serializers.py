from rest_framework import serializers
from tasks.models import Task, Category, Priority, ServiceType


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            "id",
            "category",
            "service_type",
            "immediate_resolution",
            "priority",
            "action_taken",
            "details",
            "expectation",
            "department",
            "date",
            "updated"
        ]
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
