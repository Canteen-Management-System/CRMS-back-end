from turtle import position
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class Department(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self) -> str:
        return self.name


class JobTitle(models.Model):
    position = models.CharField(max_length=60)
    department = models.ForeignKey(
        Department, on_delete=models.DO_NOTHING, blank=True)

    def __str__(self) -> str:
        return self.position


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    position = models.ForeignKey(
        JobTitle, on_delete=models.CASCADE, null=True)
    phone = PhoneNumberField(blank=True)
    birthday = models.DateField(
        help_text="Your birthday", blank=True, null=True)

    def __str__(self) -> str:
        return self.username
