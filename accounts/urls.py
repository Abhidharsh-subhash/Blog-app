from .import views
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('jwt/create/', TokenObtainPairView.as_view(), name='jwt_create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(),name='token_verify'),
    path('SignUpView/',views.SignUpView.as_view(),name='SignUpView'),
    path('LoginView/',views.LoginView.as_view(),name='LoginView'),
]