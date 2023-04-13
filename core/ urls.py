from django.urls import path
from .views import UserRegistrationView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]

