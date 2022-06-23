from ast import mod
from unicodedata import category
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
# ( Request For Quotation , appointment , technical support )


class Task(models.Model):
    # CATEGORY = [('RFQ', "Request For Quotation"),
    #             ('APT', 'Appointment'), ('TS', 'Technical Support')]
    # SERVICES = []
    # PRIORITIES = []
    # name = models.CharField(max_length=255)
    # company = models.CharField(max_length=255, blank=True, null=True)

    category = models.CharField(max_length=255)
    service_type = models.CharField(max_length=255)
    priority = models.CharField(max_length=255)
    immediate_resolution = models.BooleanField()
    action_taken = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    details = models.TextField()
    expectation = models.TextField()
    department = models.CharField(max_length=255)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
