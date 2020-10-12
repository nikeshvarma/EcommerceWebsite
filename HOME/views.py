from django.views.generic import TemplateView
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


class AboutView(TemplateView):
    template_name = 'home/about.html'


class ContactView(TemplateView):
    template_name = 'home/contact.html'
