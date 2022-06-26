from django.urls import path
from tasks.api.viewset import (
    TaskDetail,
    TasksList,
    CategoryDetail,
    CategoryList,
    PriorityDetail,
    PriorityList,
    ServiceTypeList,
    ServiceTypeDetail
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    # Tasks Lists and Details
    path('tasks-list', TasksList.as_view(), name='tasks_list'),
    path('task-detail/<int:pk>', TaskDetail.as_view(), name='task_detail'),

    # Category Lists and Details
    path('category-list', CategoryList.as_view(), name='category_list'),
    path('category-detail/<int:pk>',
         CategoryDetail.as_view(), name='category_detail'),

    # Priority Lists and Details
    path('priority-list', PriorityList.as_view(), name='priority_list'),
    path('priority-detail/<int:pk>',
         PriorityDetail.as_view(), name='priority_detail'),

    # Service Type Lists and Details
    path('service-type-list', ServiceTypeList.as_view(), name='service_type_list'),
    path('service-type-detail/<int:pk>',
         ServiceTypeDetail.as_view(), name='service_type_detail'),
    # Access Token
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
