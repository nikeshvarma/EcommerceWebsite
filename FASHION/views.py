from django.views.generic import ListView
from PRODUCTS.models import Product


class FashionHomeView(ListView):
    template_name = 'grocery/grocery_main.html'
    queryset = Product.objects.filter(product_type__product_type='Fashion')
    paginate_by = 20
