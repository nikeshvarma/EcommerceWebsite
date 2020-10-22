from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, TemplateView, ListView
from django.contrib.auth import get_user_model

from ORDER.models import Order, ProductOrdered
from ORDER.forms import OrderStatusForm
from PRODUCTS.models import Product
from .models import Shop
from ORDER.models import TransactionDetails
from .forms import SellerRegisterForm, BankDetailsForm

User = get_user_model()


@method_decorator([login_required, user_passes_test(lambda u: not u.is_seller)], name='dispatch')
class CreateSeller(CreateView):
    template_name = 'seller/seller_registration.html'
    form_class = SellerRegisterForm
    queryset = Shop.objects.all()

    def form_valid(self, form):
        postForm = form.save(commit=False)
        user = get_object_or_404(User, id=self.request.user.id)
        user.is_seller = True
        user.save()
        postForm.shop_owner_id = self.request.user.id
        postForm.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('bank_details')


@method_decorator([login_required, user_passes_test(lambda u: u.is_seller, login_url='/seller/register-shop/')], name='dispatch')
class BankInfoView(CreateView):
    template_name = 'seller/seller_bank_details.html'
    queryset = Shop.objects.all()
    form_class = BankDetailsForm

    def form_valid(self, form):
        postForm = form.save(commit=False)
        postForm.shop_owner = get_object_or_404(Shop, shop_owner_id=self.request.user.id)
        postForm.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('seller_home')


@method_decorator([login_required, user_passes_test(lambda u: u.is_seller, login_url='/seller/register-shop/')], name='dispatch')
class SellerProfileView(TemplateView):
    template_name = 'seller/seller_profile.html'


@method_decorator([login_required, user_passes_test(lambda u: u.is_seller, login_url='/seller/register-shop/')], name='dispatch')
class SellerHomeView(TemplateView):
    template_name = 'seller/seller_home.html'

    def get_context_data(self, **kwargs):
        context = super(SellerHomeView, self).get_context_data()
        # Order Section
        context['orders'] = Order.objects.filter(product__product_shop__shop_owner=self.request.user).count()

        # Listing Section
        context['listed'] = Product.objects.filter(product_shop__shop_owner=self.request.user).count()
        context['live'] = Product.objects.filter(product_shop__shop_owner=self.request.user, is_product_live=True).count()
        context['verified'] = Product.objects.filter(product_shop__shop_owner=self.request.user, is_product_verified=True).count()
        context['non_verified'] = Product.objects.filter(product_shop__shop_owner=self.request.user, is_product_verified=False).count()

        return context


@method_decorator([login_required, user_passes_test(lambda u: u.is_seller, login_url='/seller/register-shop/')], name='dispatch')
class SellerOrdersView(ListView):
    template_name = 'seller/seller_orders.html'
    paginate_by = 10

    def get_queryset(self):
        orders = Order.objects.filter(product__product_shop__shop_owner=self.request.user)
        products = ProductOrdered.objects.filter(order__in=orders).order_by('-order_id')
        return products

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SellerOrdersView, self).get_context_data()
        context['orderStatusForm'] = OrderStatusForm
        return context


@method_decorator([login_required, user_passes_test(lambda u: u.is_seller, login_url='/seller/register-shop/')], name='dispatch')
class SellerPaymentView(TemplateView):
    template_name = 'seller/seller_payments.html'

    def get_context_data(self, **kwargs):
        context = super(SellerPaymentView, self).get_context_data()
        context['transaction'] = TransactionDetails.objects.get(order_id=kwargs['order_id'])
        return context


@login_required
def update_order_status(request):
    postForm = OrderStatusForm(request.POST, instance=Order.objects.get(pk=request.POST.get('order_id')))
    if postForm.is_valid():
        postForm.save()
    return redirect('seller_orders')
