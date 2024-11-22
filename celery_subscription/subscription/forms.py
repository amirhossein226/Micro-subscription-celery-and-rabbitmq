from django import forms
from .tasks import match_address_task


class SubscriptionForm(forms.Form):
    name = forms.CharField(label='Name')
    address = forms.CharField(label='Address')
    postalcode = forms.CharField(label='Postal Code')
    city = forms.CharField(label='City')
    country = forms.CharField(label='Country')
    email = forms.EmailField(label='Email')

    def match_address(self):
        data = self.data_as_dict()
        match_address_task.delay(data)

    def data_as_dict(self):
        cd = self.cleaned_data
        as_dict = {
            'name': cd['name'],
            'address': cd['address'],
            'postalcode': cd['postalcode'],
            'city': cd['city'],
            'country': cd['country'],
            'email': cd['email']
        }
        return as_dict
