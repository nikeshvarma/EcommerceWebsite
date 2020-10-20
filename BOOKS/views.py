from django.views.generic import ListView
from PRODUCTS.models import Product


class BookHomeView(ListView):
    template_name = 'books/books_main.html'
    queryset = Product.objects.filter(product_type__product_type='Books')
    paginate_by = 20
