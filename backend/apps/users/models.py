from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_researcher = models.BooleanField(default=False)
    is_analyst = models.BooleanField(default=False)
    department = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    
    def __str__(self):
        return self.get_full_name() or self.username
