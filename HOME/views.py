from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, DetailView

from LAPTOP.models import LaptopDetails
from PHONES.models import PhoneDetails
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


class ProductDetailView(DetailView):
    template_name = 'home/product_detail_page.html'

    def get_object(self, queryset=None):
        item = get_object_or_404(Product, id=self.kwargs['id'])
        return item

    def get_context_data(self, **kwargs):
        model = self.get_model(str(self.object.product_type))
        details = model.objects.get(pk=self.kwargs['id'])
        context = {
            'details': details,
            'product': self.get_object()
        }
        return context

    # Always modified it after adding a new product type
    def get_model(self, product_type):
        if product_type == 'Mobiles':
            return PhoneDetails
        elif product_type == 'Laptops':
            return LaptopDetails


class AboutView(TemplateView):
    template_name = 'home/about.html'


class ContactView(TemplateView):
    template_name = 'home/contact.html'
