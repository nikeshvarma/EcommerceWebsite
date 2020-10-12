from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.views.generic import UpdateView, TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from PRODUCTS.models import Product
from .models import UserProfile, UserCart
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


@csrf_exempt
def updatecart(request):
    productID = request.POST.get('id')
    action = request.POST.get('action')
    if action == 'add':
        cart, created = UserCart.objects.get_or_create(user=request.user, cart_item=get_object_or_404(Product, id=productID), quantity=1)

    return JsonResponse('Request get', safe=False)


def check_item_in_cart(request):
    if request.user.is_authenticated:
        productID = request.GET.get('id')
        if UserCart.objects.filter(user=request.user, cart_item_id=productID).exists():
            return JsonResponse('found', safe=False)
        else:
            return JsonResponse('not found', safe=False)
