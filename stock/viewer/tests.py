import sys
import os

module_parent_dir_path = os.path.abspath(os.path.join(__file__,"../"))  # Make all local  parallel to stock apps
sys.path.insert(1, module_parent_dir_path)    # Do not replace sys.path[0], insert just after it


from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from viewer.loader import Loader
from viewer.models import StockQuotes


# Create your tests here.
class TestLoader(TestCase):
    def setUp(self):
        self.loader = Loader()

    def test_len(self):
        courses = self.loader.get_courses()
        codes = self.loader.get_codes()
        titles = self.loader.get_titles()
        self.assertEqual(len(codes), len(courses), len(titles))


class TestView(APITestCase):
    def setUp(self):
        quote = StockQuotes.objects.create(name="test", code="T01", price=202.2)
        quote.save()
        self.url = reverse("data-list")

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['name'], 'test')

    def test_post(self):
        data ={'name':'Testname', 'code':'TESTCODE', 'price':25.02}
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, 405)