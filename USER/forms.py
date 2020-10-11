from django import forms
from .models import UserProfile


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].required = False

    class Meta:
        model = UserProfile
        fields = '__all__'

        labels = {
            'name': 'Full Name',
            'phone_number': 'Mobile Number',
            'delivery_address_1': 'Delivery Address',
            'delivery_address_2': 'Delivery Address',
        }

        widgets = {
            'user': forms.HiddenInput(attrs={'required': ''}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'pattern': '^[a-zA-Z_ ]*$', 'title': 'Enter A Valid Name'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'type': 'tel', 'pattern': '^[6-9]\d{9}$', 'title': 'Enter A Valid Phone Number'}),
            'delivery_address_1': forms.Textarea(attrs={'class': 'form-control'}),
            'delivery_address_2': forms.Textarea(attrs={'class': 'form-control'}),
        }
