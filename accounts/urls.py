from django.urls import include, path
from accounts.api.viewset import CustomTokenObtainPairView

urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token')
]
