from rest_framework import serializers
from .models import Analysis, FakeDetectionResult

class AnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analysis
        fields = ['id', 'profile', 'analysis_type', 'result', 'confidence_score', 'created_at']

class FakeDetectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FakeDetectionResult
        fields = ['id', 'profile', 'is_fake', 'confidence', 'factors', 'created_at']
