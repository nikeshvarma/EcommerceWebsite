from django.views.generic import ListView
from PRODUCTS.models import Product


class GroceryHomeView(ListView):
    template_name = 'grocery/grocery_main.html'
    queryset = Product.objects.filter(product_type__product_type='Grocery')
    paginate_by = 20
