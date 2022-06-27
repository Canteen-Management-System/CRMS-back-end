from django.urls import include, path


from clients.api.viewset import ClientViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



urlpatterns = [
   path('clients', ClientViewSet.as_view() , name= 'clients'),
]