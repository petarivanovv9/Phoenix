from django.test import Client
from django.core.urlresolvers import reverse

from django.test import TestCase

from django.contrib.auth.models import User


class TestWebsite(TestCase):

    def setUp(self):
        self.client = Client()

    def test_index(self):
        url = reverse('website:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_login_from_active_user(self):
        pass

    def test_login_from_unactive_user(self):
        pass

    def test_login_with_invalid_data(self):
        pass

    def test_login_wrong_pass(self):
        pass

    def test_logout(self):
        pass

    def test_logout_login_required(self):
        pass

    def test_register_get_query(self):
        pass

    def test_register_if_not_registered(self):
        pass
