from django.utils.translation import ugettext as _
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.views.generic import FormView
from .forms import SignUpForm

User = get_user_model()


class Login(LoginView):
    template_name = 'accounts/loginpage.html'


class SignUp(FormView):
    form_class = SignUpForm
    success_url = '/user/profile/update'
    template_name = 'accounts/signuppage.html'

    def form_valid(self, form):
        if not User.objects.filter(email=form.cleaned_data['email']).exists():
            if form.cleaned_data['password'] == form.cleaned_data['confirm_password']:
                user = self.create_user(form.cleaned_data)
                login(self.request, user)
                return super(SignUp, self).form_valid(form)
            else:
                messages.warning(self.request, 'Password Not Match')
                return redirect('signup_page')
        else:
            messages.warning(self.request, 'Account Already Exists')
            return redirect('login_page')

    def create_user(self, form):
        user = User.objects.create_user(
            email=form['email'],
            password=form['password']
        )
        user.save()
        return user


def logout_user(request):
    logout(request)
    return redirect('home_page')


def check_register_email(request):
    email = request.GET.get('email', None)
    data = {
        'is_registered': User.objects.filter(email=email).exists()
    }
    return JsonResponse(data)
