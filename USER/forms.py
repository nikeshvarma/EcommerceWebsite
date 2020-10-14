from django import forms
from .models import UserProfile


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].required = False

    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ['pincode', 'state', 'city', 'address', 'landmark']

        labels = {
            'name': 'Full Name',
            'phone_number': 'Mobile Number',
        }

        widgets = {
            'user': forms.HiddenInput(attrs={'required': ''}),
            'gender': forms.RadioSelect(attrs={'type': 'radio', 'class': 'list-unstyled'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'pattern': '^[a-zA-Z_ ]*$', 'title': 'Enter A Valid Name'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'type': 'tel', 'pattern': '^[6-9]\d{9}$', 'title': 'Enter A Valid Phone Number'}),
        }


class AddressForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].required = False

    field_order = ['user', 'address', 'landmark', 'pincode', 'city', 'state']

    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ['name', 'phone_number', 'gender']

        widgets = {
            'user': forms.HiddenInput(attrs={'required': ''}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Flat No. / House No.'}),
            'landmark': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Landmark'}),
            'pincode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Area Pincode'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}),
        }
