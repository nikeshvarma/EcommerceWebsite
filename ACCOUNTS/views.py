from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.shortcuts import redirect
from django.contrib.auth import logout, login
from django.urls import reverse
from django.views.generic import FormView

from USER.models import UserCart
from .forms import SignUpForm

User = get_user_model()


class Login(LoginView):
    template_name = 'accounts/loginpage.html'

    def get_success_url(self):
        cart = self.request.session.get('cart', False)
        if cart:
            for item, quantity in cart.items():
                UserCart.objects.update_or_create(
                    user=self.request.user,
                    cart_item_id=item,
                    quantity=quantity
                )
        nextURL = self.request.POST.get('next', False)
        if nextURL:
            return nextURL
        else:
            return reverse('home_page')


class SignUp(FormView):
    form_class = SignUpForm
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

    def get_success_url(self):
        cart = self.request.session.get('cart', False)
        if cart:
            for item, quantity in cart.items():
                UserCart.objects.update_or_create(
                    user=self.request.user,
                    cart_item_id=item,
                    quantity=quantity
                )
        return reverse('profile_page')


def logout_user(request):
    logout(request)
    return redirect('home_page')


def check_register_email(request):
    email = request.GET.get('email', None)
    data = {
        'is_registered': User.objects.filter(email=email).exists()
    }
    return JsonResponse(data)
