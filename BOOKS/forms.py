from django import forms
from .models import BookDetails


class BookDetailsUpdateForm(forms.ModelForm):
    class Meta:
        model = BookDetails
        fields = '__all__'
        exclude = ['product']
