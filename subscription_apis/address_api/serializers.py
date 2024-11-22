from rest_framework.serializers import ModelSerializer
from .models import Address


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = ('name', 'address', 'postalcode', 'city', 'country', 'email')
