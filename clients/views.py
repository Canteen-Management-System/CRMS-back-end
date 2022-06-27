from django.urls import include, path
from api.viewset import ClientViewSet

urlpatterns = [
   path('clients-list', ClientViewSet.as_view , name= 'client-list'),
]
