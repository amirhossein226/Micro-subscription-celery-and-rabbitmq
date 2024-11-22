from django import forms
from .producer import match_address_task


class SubscriptionForm(forms.Form):
    name = forms.CharField(label='Name')
    address = forms.CharField(label='Address')
    postalcode = forms.CharField(label='Postal Code')
    city = forms.CharField(label='City')
    country = forms.CharField(label='Country')
    email = forms.EmailField(label='Email')

    def call_match(self):
        data = self.as_dict()
        match_address_task(data)

    def as_dict(self):
        cd = self.cleaned_data
        data = {
            'name': cd['name'],
            'address': cd['address'],
            'postalcode': cd['postalcode'],
            'city': cd['city'],
            'country': cd['country'],
            'email': cd['email']
        }

        return data
