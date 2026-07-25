from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'id', 'username', 'full_name', 'bio', 'followers', 'following',
            'posts', 'profile_pic_url', 'verified', 'is_private', 'website',
            'email', 'phone', 'last_scanned', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
