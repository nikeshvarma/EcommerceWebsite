from django import forms
from .models import ShirtDetails


class ShirtDetailsUpdateForm(forms.ModelForm):
    class Meta:
        model = ShirtDetails
        fields = '__all__'
        exclude = ['product']
