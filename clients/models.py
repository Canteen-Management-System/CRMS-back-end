from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth import get_user_model

class Client(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = PhoneNumberField(blank=True, unique =True)
    email = models.EmailField(max_length=255,unique = True)
    address = models.CharField(max_length=255)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    REQUIRED_FIELDS =["full_name", "phone_number"]

