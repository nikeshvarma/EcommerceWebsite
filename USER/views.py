from django.contrib import messages
from django.urls import reverse
from django.views.generic import UpdateView, TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import UserProfile
from USER.forms import ProfileForm


@method_decorator(login_required, name='dispatch')
class ProfileView(UpdateView):
    form_class = ProfileForm
    template_name = 'user/profile_page.html'

    def get_object(self, queryset=None):
        user = UserProfile.objects.get(user_id=self.request.user.id)
        return user

    def get_success_url(self):
        messages.success(self.request, 'Profile update successfully')
        return reverse('profile_page')


class CartView(TemplateView):
    template_name = 'user/cart.html'
