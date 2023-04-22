from django.contrib.auth import login, authenticate, logout

from rest_framework import status, generics, permissions
from rest_framework.response import Response

from core.models import User
from core.serializers import LoginSerializer, UserSerializer, CreateUserSerializer, UpdatePasswordSerializer


class SignUpView(generics.CreateAPIView):
    """
    View для регистрации (создания пользователя в системе) пользователя
    """
    serializer_class = CreateUserSerializer


class LoginView(generics.CreateAPIView):
    """
    View для авторизации пользователя
    """
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        login(request=self.request, user=serializer.save())
        # headers = self.get_success_headers(serializer.data)
        # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.data)


class ProfileView(generics.RetrieveUpdateDestroyAPIView):
    """
    View для получения, обновления данных пользователя и логаута
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_object(self):
        return self.request.user

    def perform_destroy(self, request, *args, **kwargs):
        logout(self.request)


class UpdatePasswordView(generics.UpdateAPIView):
    """View для смены пароля"""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UpdatePasswordSerializer
    model = User

    def get_object(self):
        return self.request.user