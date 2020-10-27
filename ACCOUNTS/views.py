from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import logout, login
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes, force_text
from django.views.generic import FormView
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from USER.models import UserCart
from .forms import SignUpForm
from .token import account_activation_token

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
                self.verify_email(user, form.cleaned_data['email'])
                self.send_mail(form.cleaned_data['email'])
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
            password=form['password'],
            is_active=False
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
        return reverse('login_page')

    def verify_email(self, user, email):
        current_site = get_current_site(self.request)
        mail_subject = 'Activate Your Account.'
        message = render_to_string(
            'accounts/account_activate_email.html',
            {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user)
            }
        )
        to_email = email
        send_mail(mail_subject, message, 'onlinestore2020@gmail.com', [to_email])
        messages.success(self.request, 'Activate your account by clicking on link sent on your registered email address.')

    def send_mail(self, email):
        send_mail(
            subject='Welcome to OnlineStore!',
            message='Hello ' + email + '! ' +
                    'We’re so excited that you’ve decided to choose onlinestore.com. ' +
                    'You can expect to hear from us <<X>> times a month with special offers, product updates, and more. ' +
                    'Contact us at helponlinestore@gmail.com if you have any questions.',
            from_email='helponlinestore2020@gmail.com',
            recipient_list=[str(email)]
        )


def logout_user(request):
    logout(request)
    return redirect('home_page')


def check_register_email(request):
    email = request.GET.get('email', None)
    data = {
        'is_registered': User.objects.filter(email=email).exists()
    }
    return JsonResponse(data)


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Thank you ! Your account activated. Now you can login your account.')
        return redirect('login_page')
    else:
        return HttpResponse('Activation link is invalid!')
