from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Department, JobTitle, Role
from django.contrib.auth.admin import UserAdmin


@admin.register(JobTitle)
class JobTitleAdmin(admin.ModelAdmin):
    model = JobTitle
    list_display = ['id', 'position', 'department']


@admin.register(Department)
class DepartmentsAdmin(admin.ModelAdmin):
    model = Department


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    model = Role


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['id',"first_name",
                    "role", 'position', 'email']

    fieldsets = UserAdmin.fieldsets + \
        (("User Info", {"fields": [
         'position', 'phone', 'birthday', 'role', 'department']}),)
