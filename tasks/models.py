from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import Department, CustomUser
from clients.models import Client


class Category(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.category

    def __repr__(self) -> str:
        return self.category


class ServiceType(models.Model):
    service = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.service

    def __repr__(self) -> str:
        return self.service


class Priority(models.Model):
    priority = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.priority

    def __repr__(self) -> str:
        return self.priority


def get_department_employees(department):
    employees = CustomUser.objects.filter(department=department)
    return employees


def get_department_staff():
    return Department.objects.all()


class Task(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)

    immediate_resolution = models.BooleanField()
    action_taken = models.TextField()
    details = models.TextField()
    expectation = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    assign_to = models.IntegerField()
    REQUIRED_FIELDS = ['category', 'service_type', 'priority', 'department']
