from rest_framework import serializers
from .models import Relationship

class RelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relationship
        fields = ['id', 'source_profile', 'target_profile', 'relationship_type', 'interaction_count', 'created_at']
