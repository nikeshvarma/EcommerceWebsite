from django import forms
from .models import LaptopDetails


class LaptopDetailUpdateForm(forms.ModelForm):
    class Meta:
        model = LaptopDetails
        fields = '__all__'
        exclude = ['product']
