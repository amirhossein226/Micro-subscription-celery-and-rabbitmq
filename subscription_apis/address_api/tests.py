# from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Address
# Create your tests here.


class AddressTestCase(APITestCase):
    url = 'http://127.0.0.1:8000/api/v1/addresses/'

    def setUp(self):
        data = {
            'name': 'abol',
            'address': 'abhar amidabad khorram',
            'postalcode': 'sldjf3243ljln',
            'city': 'zanjan',
            'country': 'Iran',
            'email': 'amir@gmail.com'
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['name'], 'abol')

        self.address = Address.objects.get()

    def test_get_address(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)

    def test_partial_update_address(self):
        data = {'email': 'abol@gmail.com', }
        url = self.url + str(self.address.id) + '/'
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['email'], 'abol@gmail.com')

    def test_complete_update_address(self):
        data = {
            'name': 'amir',
            'address': 'adj asjf kloi dfsdf',
            'postalcode': 'asdfjklaj323',
            'city': 'kkkkkk',
            'country': 'England',
            'email': 'amir@gmail.com'
        }
        url = self.url + str(self.address.id) + '/'
        response = self.client.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'], 'amir')
        self.assertEqual(response.json()['city'], 'kkkkkk')
        self.assertEqual(response.json()['country'], 'England')

    def test_delete_address(self):
        url = self.url + str(self.address.id) + '/'

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class BorderTestingAddress(APITestCase):
    data = {
        'name': 'ahmad',
        'address': 'zanjan abhar taleghani-shomaly',
        'postalcode': 'abcdefghij12345',
        'city': 'Zanjan',
        'country': 'Iran',
        'email': 'ahamd@gmail.com'
    }
    url = 'http://127.0.0.1:8001/api/v1/addresses/'

    def test_valid_postalcode_creation(self):
        valid_data = self.data.copy()
        response = self.client.post(self.url, valid_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_invalid_postalcode_creation(self):
        invalid_data = self.data.copy()
        invalid_data.update({'postalcode': 'abcdefghij123456'})
        response = self.client.post(self.url, invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
