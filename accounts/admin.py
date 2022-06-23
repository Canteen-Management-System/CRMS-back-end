from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Department, JobTitle
# from .forms import CustomUserChangeForm
# from .forms import CustomUserCreationForm
# Register your models here.


@admin.register(JobTitle)
class JobTitleAdmin(admin.ModelAdmin):
    model = JobTitle
    list_display = ['position', 'department']


@admin.register(Department)
class DepartmentsAdmin(admin.ModelAdmin):
    model = Department


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ["username", "first_name",
                    "last_name", 'position']

    fieldsets = UserAdmin.fieldsets + \
        (("User Info", {"fields": ['position', 'phone', 'birthday']}),)
