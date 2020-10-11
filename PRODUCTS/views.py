from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth import get_user_model
from LAPTOP.forms import LaptopDetailUpdateForm
from PHONES.forms import PhoneDetailsUpdateForm
from .models import Product
from .forms import ListProductForm, UpdateProductForm

User = get_user_model()


@method_decorator([login_required, user_passes_test(lambda u: u.is_seller, login_url='/seller/register-shop/')], name='dispatch')
class ListProductView(CreateView):
    template_name = 'products/listing_page.html'
    queryset = Product.objects.all()
    form_class = ListProductForm

    def form_valid(self, form):
        postForm = form.save(commit=False)
        postForm.product_shop_id = self.request.user.shop.id
        postForm.save()
        messages.success(self.request, 'Product added to inventory.')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('list_product')


@method_decorator([login_required, user_passes_test(lambda u: u.is_seller, login_url='/seller/register-shop/')], name='dispatch')
class InventoryListView(ListView):
    template_name = 'products/inventory_page.html'
    model = Product
    paginate_by = 20

    def get_queryset(self):
        queryset = Product.objects.filter(product_shop_id=self.request.user.shop.id)
        return queryset


@method_decorator([login_required, user_passes_test(lambda u: u.is_seller, login_url='/seller/register-shop/')], name='dispatch')
class UpdateProductView(UpdateView):
    template_name = 'products/update_listing_page.html'
    form_class = UpdateProductForm

    def get(self, request, *args, **kwargs):
        if self.get_object().product_shop_id == self.request.user.shop.id:
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponse("You don't have access to this page...")

    def form_valid(self, form):
        if form.cleaned_data['is_product_live'] and self.object.is_product_verified:
            messages.success(self.request, 'Yehh your product is live ...')
            return super(UpdateProductView, self).form_valid(form)
        else:
            postForm = form.save(commit=False)
            postForm.is_product_live = False
            postForm.save()
            messages.warning(self.request, "You can't set product to live until is verified")
            return super(UpdateProductView, self).form_valid(form)

    def get_object(self, queryset=None):
        product = get_object_or_404(Product, id=self.kwargs['id'])
        return product

    def get_success_url(self):
        return reverse('inventory_page')

    def get_context_data(self, **kwargs):
        context = super(UpdateProductView, self).get_context_data()
        context['image'] = self.object.product_home_img
        return context


@method_decorator([login_required, user_passes_test(lambda u: u.is_seller, login_url='/seller/register-shop/')], name='dispatch')
class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('inventory_page')
    template_name = 'products/confirm_listing_delete.html'

    def get_object(self, queryset=None):
        product = get_object_or_404(Product, id=self.kwargs['id'])
        return product


@method_decorator([login_required, user_passes_test(lambda u: u.is_seller, login_url='/seller/register-shop/')], name='dispatch')
class ProductDetailUpdateView(UpdateView):
    template_name = 'products/add_update_product_details.html'

    def get(self, request, *args, **kwargs):
        if self.get_shop_id().product_shop_id == self.request.user.shop.id:
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponse("You don't have access to this page...")

    def get_form_class(self):
        category = self.kwargs['category']
        if category == 'Mobiles':
            return PhoneDetailsUpdateForm
        elif category == 'Laptops':
            return LaptopDetailUpdateForm

    def get_object(self, queryset=None):
        model = self.get_form_class().Meta.model
        product, created = model.objects.get_or_create(pk=self.kwargs['id'], product_id=self.kwargs['id'])
        return product

    def get_success_url(self):
        messages.success(self.request, 'Details Updated')
        return reverse('inventory_page')

    def get_shop_id(self):
        product_id = get_object_or_404(Product, id=self.kwargs['id'])
        return product_id
