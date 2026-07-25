from django.test import TestCase
from apps.profile.models import Profile

class ProfileModelTest(TestCase):
    def setUp(self):
        self.profile = Profile.objects.create(
            username='testuser',
            full_name='Test User',
            followers=1000,
            following=500
        )
    
    def test_profile_creation(self):
        self.assertEqual(self.profile.username, 'testuser')
        self.assertEqual(self.profile.followers, 1000)
    
    def test_profile_str(self):
        self.assertEqual(str(self.profile), 'testuser')
