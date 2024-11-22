import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from time import sleep


class TestSubscriptionView(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.headless = False
        self.driver = webdriver.Chrome(options=options)
        self.driver.get('http://127.0.0.1:8000/subscription/form/')

        con_string = "mongodb+srv://django-restful-api:LRVVgvzYLcnh4B6y@cluster0.jbyh4.mongodb.net/"
        client = MongoClient(con_string, server_api=ServerApi('1'))
        db = client['Subscription']
        self.coll = db['address_api_address']

    def test_subscription(self):
        driver = self.driver
        coll = self.coll

        driver.find_element(By.NAME, 'name').send_keys('Faeze')
        driver.find_element(By.NAME, 'address').send_keys(
            'Tehran sohrevardy babaii')
        driver.find_element(By.NAME, 'postalcode').send_keys('lsdjf3242')
        driver.find_element(By.NAME, 'city').send_keys('Lvizan')
        driver.find_element(By.NAME, 'country').send_keys('Iran')
        driver.find_element(By.NAME, 'email').send_keys('faeze@gmail.com')
        driver.find_element(By.NAME, 'submit').click()

        sleep(4)
        success_header = driver.find_element(By.NAME, 'success_header').text
        self.assertIn('Thanks', success_header)

        last_database_record = coll.find().sort('id', -1).limit(1)
        self.assertEqual(last_database_record['name'], 'Faeze')
        # coll.delete_on({'id': last_database_record['id']})

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)
