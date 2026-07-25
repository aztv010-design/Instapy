from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    username = models.CharField(max_length=255, unique=True, db_index=True)
    full_name = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)
    posts = models.IntegerField(default=0)
    profile_pic_url = models.URLField(blank=True)
    verified = models.BooleanField(default=False)
    is_private = models.BooleanField(default=False)
    website = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    last_scanned = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-last_scanned']
        indexes = [
            models.Index(fields=['username']),
            models.Index(fields=['created_at']),
        ]
    
    def __str__(self):
        return self.username
