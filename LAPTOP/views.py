from django.views.generic import ListView
from PRODUCTS.models import Product


class LaptopHomeView(ListView):
    template_name = 'laptops/laptop_main.html'
    queryset = Product.objects.filter(product_type__product_type='Laptops')
    paginate_by = 20
