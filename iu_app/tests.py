from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Kiosk

class KioskListViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='login', password='pass')
        self.client.login(username='login', password='pass')
        self.kiosk_a = Kiosk.objects.create(name='A kiosk')
        self.kiosk_b = Kiosk.objects.create(name='B kiosk')

    def test_kiosk_list_view(self):
        # arrange
        expected_result = [{'name': self.kiosk_a.name}]
        # act
        response = self.client.get(reverse('kiosks'))
        # assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, expected_result)

    def test_kiosk_list_view_superuser(self):
        # arrange
        self.user.is_superuser = True
        self.user.save()
        expected_result = [
            {'name': self.kiosk_a.name},
            {'name': self.kiosk_b.name},
        ]
        # act
        response = self.client.get(reverse('kiosks'))
        # assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, expected_result)
