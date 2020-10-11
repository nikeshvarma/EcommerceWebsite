from django import forms
from .models import Product


class ListProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['product_shop', 'is_product_live', 'is_product_verified']


class UpdateProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UpdateProductForm, self).__init__(*args, **kwargs)
        self.fields['is_product_live'].label = 'Live'

    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['product_shop', 'is_product_verified', 'product_category', 'product_type']
