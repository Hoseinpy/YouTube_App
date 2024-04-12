import time
import os
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .forms import LoginForm, SingupForm, ForgetPasswordForm, ResetPasswordForm
from django.views import View
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string
from utils.send_email import send_email

User = get_user_model()


@method_decorator(csrf_exempt, name='dispatch')
class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'accounts/login_page.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('index-page')

            form.add_error('', 'email or password is incorrect')

        return render(request, 'accounts/login_page.html', {'form': form})


@method_decorator(csrf_exempt, name='dispatch')
class SingupView(View):
    def get(self, request):
        form = SingupForm()
        return render(request, 'accounts/singup_page.html', {'form': form})

    def post(self, request):
        form = SingupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                form.add_error('', 'email is already exists')
                return render(request, 'accounts/singup_page.html', {'form': form})

            user = User.objects.create(email=email, verify_code=get_random_string(72))
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            time.sleep(2)
            return redirect('login-page')

        return render(request, 'accounts/singup_page.html', {'form': form})


@method_decorator(csrf_exempt, name='dispatch')
class ForgotPasswordView(View):
    def get(self, request):
        form = ForgetPasswordForm()
        return render(request, 'accounts/forget_password.html', {'form': form})

    def post(self, request):
        form = ForgetPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            if user := User.objects.filter(email=email).first():
                send_email(subject='forget password', context={'user':user}, to=email, template_name='accounts/forget_pass_email_body.html')
                return HttpResponse('<h2><center>Forgot password form has been sent to your email, check your email</center></h2>')

            form.add_error('', 'email not found')

        return render(request, 'accounts/forget_password.html', {'form': form})


@method_decorator(csrf_exempt, name='dispatch')
class ForgotPasswordVerifyView(View):

    def get(self, request, code):
        user = User.objects.filter(verify_code=code).first()
        if user is not None:
            form = ResetPasswordForm()
            return render(request, 'accounts/forgot_password_verify.html', {'form': form, 'user': user})

        return render(request, 'accounts/404.html')

    def post(self, request, code):
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            user = User.objects.filter(verify_code=code).first()
            print(form.cleaned_data.get('password'))
            user.set_password(form.cleaned_data.get('password'))
            user.verify_code = get_random_string(72)
            user.save()
            return redirect('login-page')

        return render(request, 'accounts/forgot_password_verify.html', {'form': form})