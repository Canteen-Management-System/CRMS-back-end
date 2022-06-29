from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomUserSerializer
from accounts.models import CustomUser
from rest_framework.permissions import IsAuthenticated
from .serializers import CustomUserSerializer, CustomTokenObtainPairSerializer
from rest_framework.response import Response


class CustomUserViewSet(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        response.data['custom_key'] = 'my_custom_data'
        return response
