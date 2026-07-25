from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from apps.profile.models import Profile

class ProfileAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.force_authenticate(user=self.user)
    
    def test_scan_profile(self):
        response = self.client.post('/api/profile/scan/', {'username': 'instagram_user'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
