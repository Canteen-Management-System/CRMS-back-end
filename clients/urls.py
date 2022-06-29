from django.urls import include, path


from clients.api.viewset import ClientDetailView, ClientListView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('clients', ClientListView.as_view(), name='clients'),
    path('client-detail/<int:pk>', ClientDetailView.as_view(), name='client_detail'),
]
