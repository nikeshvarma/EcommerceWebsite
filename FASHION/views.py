from django.views.generic import ListView
from PRODUCTS.models import Product
from .models import ShirtDetails


class FashionHomeView(ListView):
    template_name = 'fashion/fashion_home.html'
    queryset = Product.objects.filter(product_type__product_type='Shirts')
    paginate_by = 20

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(FashionHomeView, self).get_context_data()
        context['products'] = {ShirtDetails.objects.get(product_id=x.id): x for x in Product.objects.filter(product_type__product_type='Shirts')}
        return context
