import os
import sys
import django

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'instapy.settings')
    django.setup()
    
    from apps.profile.models import Profile
    from apps.analysis.models import Analysis, FakeDetectionResult
    
    # Create sample profiles
    sample_profiles = [
        {'username': 'test_user_1', 'full_name': 'Test User 1', 'followers': 1000, 'following': 500},
        {'username': 'test_user_2', 'full_name': 'Test User 2', 'followers': 5000, 'following': 1000},
        {'username': 'test_user_3', 'full_name': 'Test User 3', 'followers': 10000, 'following': 2000},
    ]
    
    for profile_data in sample_profiles:
        profile, created = Profile.objects.get_or_create(
            username=profile_data['username'],
            defaults=profile_data
        )
        if created:
            print(f"Created profile: {profile.username}")
    
    print("Sample data loaded successfully!")
