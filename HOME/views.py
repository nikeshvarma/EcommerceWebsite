from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, DetailView, ListView
from django.db.models import Q

from BOOKS.models import BookDetails
from FASHION.models import ShirtDetails
from LAPTOP.models import LaptopDetails
from PHONES.models import PhoneDetails
from USER.models import UserProfile, UserCart
from .models import CarouselImage
from PRODUCTS.models import Product


class HomeView(TemplateView):
    template_name = 'home/homepage.html'

    def get_context_data(self, **kwargs):
        carousel_images = CarouselImage.objects.all()
        latest_products = Product.objects.filter(is_product_live=True, is_product_verified=True).order_by('-product_add_datetime_stamp')[:6]
        context = {
            'carousel_images': carousel_images,
            'latest_products': latest_products,
        }
        return context


class SearchView(ListView):
    template_name = 'home/search_result.html'
    paginate_by = 30

    def get_queryset(self):
        query = self.request.GET.get('q')
        queryset = Product.objects.filter(
            Q(product_name=query)
            | Q(product_name__startswith=query)
            | Q(product_name__icontains=query)
        )
        return queryset


class CategoryView(TemplateView):
    template_name = 'home/category_page.html'


class ProductDetailView(DetailView):
    template_name = 'home/product_detail_page.html'

    def get_object(self, queryset=None):
        item = get_object_or_404(Product, id=self.kwargs['id'])
        return item

    def get_context_data(self, **kwargs):
        model = self.get_model(str(self.object.product_type))
        details = model.objects.get(pk=self.kwargs['id'])
        product = self.get_object()
        discount = round(((product.product_MRP - product.product_selling_price) * 100) / product.product_MRP)
        context = {
            'details': details,
            'product': product,
            'discount': discount,
        }
        return context

    # Always modified it after adding a new product type
    def get_model(self, product_type):
        if product_type == 'Mobiles':
            return PhoneDetails
        elif product_type == 'Laptops':
            return LaptopDetails
        elif product_type == 'Books':
            return BookDetails
        elif product_type == 'Shirts':
            return ShirtDetails


@method_decorator(login_required, name='dispatch')
class CheckOutView(TemplateView):
    template_name = 'home/checkout.html'

    def get_context_data(self, **kwargs):
        context = super(CheckOutView, self).get_context_data(**kwargs)
        context['profile'] = UserProfile.objects.get(user=self.request.user)
        items = UserCart.objects.filter(user=self.request.user)
        product_id = dict([x for x in items.values_list('cart_item_id', 'quantity')])
        context['product_id'] = str(product_id)
        item_list = list(items.values_list('quantity', 'cart_item__product_selling_price'))
        billing_amount = sum([x[0] * x[1] for x in item_list])
        context['cart_items'] = items
        context['amount'] = billing_amount
        return context


class AboutView(TemplateView):
    template_name = 'home/about.html'


class ContactView(TemplateView):
    template_name = 'home/contact.html'
