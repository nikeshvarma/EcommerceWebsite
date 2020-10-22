from django.views.generic import ListView
from PRODUCTS.models import Product
from .models import BookDetails


class BookHomeView(ListView):
    template_name = 'books/books_main.html'
    queryset = Product.objects.filter(product_type__product_type='Books')
    paginate_by = 20

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BookHomeView, self).get_context_data()
        context['products'] = {BookDetails.objects.get(product_id=x.id): x for x in Product.objects.filter(product_type__product_type='Books')}
        return context
