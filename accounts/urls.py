from django.urls import path
from .views import LoginView, SingupView, ForgotPasswordView, ForgotPasswordVerifyView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login-page'),
    path('singup/', SingupView.as_view(), name='singup-page'),
    path('forget_password/', ForgotPasswordView.as_view(), name='forget-password-page'),
    path('forget_password/<str:code>', ForgotPasswordVerifyView.as_view(), name='forget-password-verify-page'),
]