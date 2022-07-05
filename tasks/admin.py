from django.contrib import admin
from .models import Task, Category, Priority, ServiceType


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    model = Task
    list_display = ['id', 'category', 'date',
                    'user', 'status', 'action_taken', 'details', 'assign_to']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ['id', 'category']


@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    model = Priority
    list_display = ['id', 'priority']


@admin.register(ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    model = ServiceType
    list_display = ['id', 'service']
