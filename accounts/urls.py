from django.urls import include, path
from accounts.api.viewset import CustomTokenObtainPairView, UsersList

urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token'),
    path('users', UsersList.as_view(), name='users_list')
]
