# from django.test import TestCase
from unittest import TestCase
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from .tasks import match_address_task, send_email_task
from time import sleep
from dotenv import load_dotenv
import os
load_dotenv()

# Create your tests here.


class TestMatchMicroservice(TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        con = os.environ.get("MONGO_CONNECTION_STRING")
        client = MongoClient(con, server_api=ServerApi('1'))
        db = client['Subscription']
        self.coll = db['address_api_address']

    def test_match_micro_creates_address(self):
        data = {
            'name': 'abol',
            'address': 'abhar mydan emamhossein',
            'postalcode': 'sdljf3242',
            'city': 'Zanjan',
            'country': 'Iran',
            'email': 'abol@gmail.com'
        }

        match_address_task.delay(data)
        sleep(3)

        address = self.coll.find().sort('id', -1).limit(1)[0]
        self.assertEqual(address['name'], data['name'])
        self.coll.delete_one({'id': address['id']})
