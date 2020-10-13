from django.contrib import messages
from django.http import JsonResponse, HttpResponse
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

    def get_context_data(self, **kwargs):
        if self.request.user.is_authenticated:
            items = UserCart.objects.filter(user=self.request.user)
            item_list = list(items.values_list('quantity', 'cart_item__product_selling_price'))
            billing_amount = sum([x[0] * x[1] for x in item_list])
            context = {'cart_items': items, 'amount': billing_amount}
            return context
        else:
            items = self.request.session.get('cart', False)
            if items:
                cart_items = {Product.objects.get(id=key): value for key, value in items.items()}
                amount = sum([item.product_selling_price * quantity for item, quantity in cart_items.items()])
                context = {'cart_items': cart_items, 'amount': amount}
                return context
            else:
                context = {}
                return context


@csrf_exempt
def updatecart(request):
    productID = request.POST.get('id')
    action = request.POST.get('action')
    if action == 'add':
        UserCart.objects.get_or_create(user=request.user, cart_item=get_object_or_404(Product, id=productID), quantity=1)
    elif action == 'increment':
        item = UserCart.objects.get(user=request.user, cart_item_id=productID)
        if item.quantity < 5:
            item.quantity += 1
            item.save()
        else:
            messages.warning(request, 'maximum quantity limit exceed.')
            return JsonResponse({'error': "maximum quantity limit exceed."}, safe=False)
    elif action == 'decrement':
        item = UserCart.objects.get(user=request.user, cart_item_id=productID)
        if item.quantity > 1:
            item.quantity -= 1
            item.save()
        else:
            messages.warning(request, "Can't reduce quantity.")
            return JsonResponse({'error': "Can't reduce quantity."}, safe=False)

    elif action == 'remove':
        item = UserCart.objects.get(user=request.user, cart_item_id=productID)
        item.delete()
        return JsonResponse({'message': 'item removed from cart'})
    return JsonResponse({'message': 'response receive'})


@csrf_exempt
def update_session_cart(request):
    productID = request.POST.get('id')
    action = request.POST.get('action')
    if action == 'add':
        if 'cart' not in request.session:
            request.session['cart'] = {productID: 1}
        else:
            cart = request.session['cart']
            cart.update({productID: 1})
        return JsonResponse({'message': 'item added'}, status=200)

    if action == 'remove':
        cart = request.session['cart']
        cart.pop(productID)
        return JsonResponse({'message': 'item removed'}, status=200)

    if action == 'increment':
        cart = request.session['cart']
        if cart[productID] < 5:
            cart[productID] += 1
        else:
            messages.warning(request, 'maximum quantity limit exceed.')
        return JsonResponse({'message': 'quantity increased'}, status=200)

    if action == 'decrement':
        cart = request.session['cart']
        if cart[productID] > 1:
            cart[productID] -= 1
        else:
            messages.info(request, "Click on Remove to remove item from cart ... ")
        return JsonResponse({'message': 'quantity increased'}, status=200)


def check_item_in_cart(request):
    productID = request.GET.get('id')
    if request.user.is_authenticated:
        if UserCart.objects.filter(user=request.user, cart_item_id=productID).exists():
            return JsonResponse('found', safe=False)
        else:
            return JsonResponse('not found', safe=False)
    else:
        cart = request.session.get('cart', False)
        if cart and productID in list(cart.keys()):
            return JsonResponse('found', safe=False)
        else:
            return JsonResponse('not found', safe=False)
