from django.views.generic import ListView
from PRODUCTS.models import Product


class FashionHomeView(ListView):
    template_name = 'fashion/fashion_home.html'
    queryset = Product.objects.filter(product_type__product_type='Shirts')
    paginate_by = 20
