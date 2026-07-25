from django.db import models
from apps.profile.models import Profile

class Geolocation(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='geolocation')
    country = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    accuracy = models.IntegerField(default=0)  # in kilometers
    last_seen_location = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.profile.username} - {self.city}, {self.country}"
