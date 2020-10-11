from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, TemplateView, UpdateView
from django.contrib.auth import get_user_model
from .models import Shop
from .forms import SellerRegisterForm

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
        return reverse('seller_home')


@method_decorator([login_required, user_passes_test(lambda u: u.is_seller, login_url='/seller/register-shop/')], name='dispatch')
class SellerProfileView(TemplateView):
    template_name = 'seller/seller_profile.html'


@method_decorator([login_required, user_passes_test(lambda u: u.is_seller, login_url='/seller/register-shop/')], name='dispatch')
class SellerHomeView(TemplateView):
    template_name = 'seller/seller_home.html'


@method_decorator([login_required, user_passes_test(lambda u: u.is_seller, login_url='/seller/register-shop/')], name='dispatch')
class SellerOrdersView(TemplateView):
    template_name = 'seller/seller_orders.html'


@method_decorator([login_required, user_passes_test(lambda u: u.is_seller, login_url='/seller/register-shop/')], name='dispatch')
class SellerPaymentView(TemplateView):
    template_name = 'seller/seller_payments.html'
