from django.contrib import admin
from django.forms import ClearableFileInput
from .models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    model = Client
    list_display= ['full_name','phone_number']
