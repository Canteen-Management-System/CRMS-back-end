from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser , PermissionsMixin, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
import uuid
from django.contrib.auth.models import User
import random

class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, employer_id, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, employer_id,  password, **other_fields)

    def create_user(self, email, employer_id,  password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, employer_id=employer_id,
                          **other_fields)
        user.set_password(password)
        user.save()
        return user



class Department(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name


class JobTitle(models.Model):
    name = models.CharField(max_length=60)
    department = models.ForeignKey(
        Department, on_delete=models.DO_NOTHING, blank=True)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name




class CustomUser(AbstractUser):
    def random_wlan_key():
      return ''.join(random.SystemRandom().choice("1234567890") for i in range(7))

    employer_id = models.CharField(max_length=10, default=random_wlan_key,unique=True)
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

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'employer_id'
    # REQUIRED_FIELDS = ['', 'first_name']


    # def __repr__(self) -> str:
    #     return self.username
