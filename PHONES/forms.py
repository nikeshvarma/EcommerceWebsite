from django import forms
from .models import PhoneDetails


class PhoneDetailsUpdateForm(forms.ModelForm):
    class Meta:
        model = PhoneDetails
        fields = '__all__'
        exclude = ['product']
