from .import views
from django.urls import path

urlpatterns = [
    path('SignUpView/',views.SignUpView.as_view(),name='SignUpView'),
    path('LoginView/',views.LoginView.as_view(),name='LoginView'),
]