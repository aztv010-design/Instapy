from django.db import models
from apps.profile.models import Profile

class Relationship(models.Model):
    source_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='outgoing_relationships')
    target_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='incoming_relationships')
    relationship_type = models.CharField(
        max_length=50,
        choices=[('follow', 'Follows'), ('followed_by', 'Followed By'), ('mutual', 'Mutual')]
    )
    interaction_count = models.IntegerField(default=0)
    last_interaction = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('source_profile', 'target_profile')
    
    def __str__(self):
        return f"{self.source_profile.username} {self.relationship_type} {self.target_profile.username}"
