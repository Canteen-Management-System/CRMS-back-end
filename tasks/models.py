from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import Department, CustomUser
from clients.models import Client
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField



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
    action_taken = models.TextField(null=True, blank=True)
    details = models.TextField(null=True, blank=True)
    expectation = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    assign_to = models.IntegerField(null=True, blank=True)
    # assign_to = models.ForeignKey(
    # CustomUser, on_delete=models.DO_NOTHING, related_name='assign_to')

    status = models.CharField(max_length=20, default='open')
    REQUIRED_FIELDS = ['category', 'service_type', 'priority', 'department']


class ClientReq(models.Model):
    client_name = models.CharField(max_length=255)
    client_company = models.CharField(max_length=255, default='')
    client_phone_number = PhoneNumberField(unique=True)
    client_email = models.EmailField(max_length=255, unique=True)
    task_category = models.CharField(max_length=255, default='')
    task_service_type = models.CharField(max_length=255, default='')
    task_details = models.TextField(null=True, blank=True)
    REQUIRED_FIELDS = ['client_name', 'client_phone_number', 'client_email', 'task_details']
