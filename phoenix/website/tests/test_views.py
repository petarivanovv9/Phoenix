import factory
from faker import Factory

from django.test import Client
from django.core.urlresolvers import reverse

from test_plus.test import TestCase

from unittest import skip

from django.contrib.auth.models import User


faker = Factory.create()


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User

    username = 'pepson'
    password = 'pepson123'
    email = faker.email()


class TestWebsite(TestCase):

    def setUp(self):
        self.client = Client()
        #self.user = UserFactory()
        self.user = User.objects.create_user(
            username=UserFactory.username,
            password=UserFactory.password,
            email=UserFactory.email
        )
        self.user.save()

    def test_index(self):
        url = reverse('website:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    #@skip("There some errors in the test")
    def test_login_from_active_user(self):
        url = reverse('website:login')
        self.user.is_active = True
        self.user.save()

        data = {
            'username': self.user.username,
            'password': UserFactory.password
        }

        #login = self.client.login(username=self.user.username, password=UserFactory.password)
        #self.assertEqual(login, True)

        response = self.client.post(url, data, follow=True)

        print(response.redirect_chain)
        #self.response_302(response)
        #response = self.client.get(url)
        self.assertContains(response, 'OR')
        self.assertRedirects(response, reverse('website:index'))

    def test_login_from_unactive_user(self):
        url = reverse('website:login')
        self.user.is_active = False
        self.user.save()
        data = {
            'username': self.user.username,
            'password': UserFactory.password
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['error'],
                         'Invalid username or password')

    def test_login_wrong_username(self):
        url = reverse('website:login')
        data = {
            'username': faker.name(),
            'password': UserFactory.password
        }

        response = self.client.post(url, data)

        self.assertEqual(response.context['error'],
                         'Invalid username or password')
        self.assertEqual(response.status_code, 200)

    def test_login_wrong_pass(self):
        url = reverse('website:login')
        data = {
            'username': self.user.email,
            'password': faker.password()
        }

        response = self.client.post(url, data)

        self.assertEqual(response.context['error'],
                         'Invalid username or password')
        self.assertEqual(response.status_code, 200)

    #@skip("There some errors in the test")
    def test_logout(self):
        self.user.is_active = True
        self.user.save()
        url = reverse('website:logout')
        print(url)
        # login = self.client.login(username=self.user.username, password=UserFactory.password)
        # self.assertEqual(login, True)
        response = self.client.get(url, follow=True)

        print(response.redirect_chain)

        #self.response_302(response)
        #self.assertContains(response, 'OR')
        #self.assertRedirects(response, reverse('website:index'))

    def test_logout_login_required(self):
        url = reverse('website:logout')
        response = self.client.get(url)

        self.response_302(response)

    def test_register_get_query(self):
        url = reverse('website:register')
        get_resp = self.client.get(url)

        self.response_200(get_resp)
        self.assertIsNotNone(get_resp.context['form'])

    def test_register_if_not_registered(self):
        data = {
            'username': 'pepo',
            'email': faker.email(),
            'password':  'pepo123',
            'password2': 'pepo123',
        }
        url = reverse('website:register')

        post_resp = self.client.post(url, data)

        self.response_302(post_resp)
        self.assertRedirects(post_resp, reverse('website:index'))

        made_user = User.objects.last()

        self.assertEqual(User.objects.filter(username=data['username']).count(), 1)
        self.assertEqual(made_user.email, data['email'])
        self.assertEqual(made_user.username, data['username'])
        self.assertTrue(made_user.check_password(data['password']))
