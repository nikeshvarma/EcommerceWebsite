from django import forms
from .models import Shop, ShopOwnerBankDetails


class SellerRegisterForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = '__all__'
        exclude = ['shop_owner', 'is_shop_verified']


class BankDetailsForm(forms.ModelForm):
    class Meta:
        model = ShopOwnerBankDetails
        fields = '__all__'
        exclude = ['shop_owner']
