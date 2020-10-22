from django.views.generic import ListView
from PRODUCTS.models import Product
from .models import LaptopDetails


class LaptopHomeView(ListView):
    template_name = 'laptops/laptop_main.html'
    queryset = Product.objects.filter(product_type__product_type='Laptops')
    paginate_by = 20

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(LaptopHomeView, self).get_context_data()
        context['products'] = {LaptopDetails.objects.get(product_id=x.id): x for x in Product.objects.filter(product_type__product_type='Laptops')}
        return context
