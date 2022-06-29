from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
import uuid
from django.contrib.auth.models import User


class Department(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name


class JobTitle(models.Model):
    position = models.CharField(max_length=60)
    department = models.ForeignKey(
        Department, on_delete=models.DO_NOTHING, blank=True)

    def __str__(self) -> str:
        return self.position

    def __repr__(self) -> str:
        return self.position


class Role(models.Model):
    role = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.role

    def __repr__(self) -> str:
        return self.role


class CustomUser(AbstractUser):

    employer_id = models.CharField(default=uuid.uuid4(
    ).hex[:7].upper(), max_length=50, editable=False, unique=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    position = models.ForeignKey(
        JobTitle, on_delete=models.CASCADE, null=True)
    phone = PhoneNumberField(blank=True)
    birthday = models.DateField(
        help_text="Your birthday", blank=True, null=True)
    department = models.ForeignKey(
        Department, on_delete=models.DO_NOTHING, null=True)
    role = models.ForeignKey(Role, on_delete=models.DO_NOTHING, null=True)
    email = models.EmailField(max_length=255)

    # USERNAME_FIELD = 'username'
