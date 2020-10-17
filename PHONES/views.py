from django.views.generic import ListView
from PRODUCTS.models import Product


class PhoneHomeView(ListView):
    template_name = 'phones/phone_main.html'
    queryset = Product.objects.filter(product_type__product_type='Mobiles')
    paginate_by = 20
