from django.views.generic import ListView
from PRODUCTS.models import Product
from .models import PhoneDetails


class PhoneHomeView(ListView):
    template_name = 'phones/phone_main.html'
    queryset = Product.objects.filter(product_type__product_type='Mobiles')
    paginate_by = 20

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PhoneHomeView, self).get_context_data()
        context['products'] = {PhoneDetails.objects.get(product_id=x.id): x for x in Product.objects.filter(product_type__product_type='Mobiles')}
        return context
