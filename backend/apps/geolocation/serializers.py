from rest_framework import serializers
from .models import Geolocation

class GeolocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geolocation
        fields = ['id', 'profile', 'country', 'city', 'latitude', 'longitude', 'accuracy', 'created_at']
