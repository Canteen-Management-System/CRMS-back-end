from django.urls import include, path


from api.viewset import CustomUserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



urlpatterns = [
   path('accounts', CustomUserViewSet.as_view , name= 'accounts'),
]