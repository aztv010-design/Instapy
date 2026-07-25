from django.db import models
from apps.profile.models import Profile

class Report(models.Model):
    REPORT_FORMATS = [
        ('pdf', 'PDF'),
        ('excel', 'Excel'),
        ('json', 'JSON'),
    ]
    
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='reports')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    format = models.CharField(max_length=50, choices=REPORT_FORMATS, default='pdf')
    file_path = models.FileField(upload_to='reports/')
    data = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.profile.username} - {self.title}"
