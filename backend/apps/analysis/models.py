from django.db import models
from apps.profile.models import Profile

class Analysis(models.Model):
    ANALYSIS_TYPES = [
        ('fake', 'Fake Account Detection'),
        ('activity', 'Activity Analysis'),
        ('engagement', 'Engagement Analysis'),
        ('sentiment', 'Sentiment Analysis'),
    ]
    
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='analyses')
    analysis_type = models.CharField(max_length=50, choices=ANALYSIS_TYPES)
    result = models.JSONField(default=dict)
    confidence_score = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Analyses'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.profile.username} - {self.get_analysis_type_display()}"

class FakeDetectionResult(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='fake_detection')
    is_fake = models.BooleanField(default=False)
    confidence = models.FloatField(default=0.0)
    factors = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.profile.username} - Fake: {self.is_fake}"
