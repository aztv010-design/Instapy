from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from apps.profile.models import Profile
from .models import FakeDetectionResult, Analysis
from .serializers import FakeDetectionSerializer, AnalysisSerializer

class FakeDetectionView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, profile_id):
        try:
            profile = Profile.objects.get(id=profile_id)
            fake_detection, created = FakeDetectionResult.objects.get_or_create(
                profile=profile,
                defaults={
                    'is_fake': False,
                    'confidence': 0.95,
                    'factors': {
                        'follower_ratio': 0.9,
                        'activity_pattern': 0.95,
                        'engagement_rate': 0.88
                    }
                }
            )
            serializer = FakeDetectionSerializer(fake_detection)
            return Response(serializer.data)
        except Profile.DoesNotExist:
            return Response(
                {'error': 'Profile not found'},
                status=status.HTTP_404_NOT_FOUND
            )

class ActivityAnalysisView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, profile_id):
        try:
            profile = Profile.objects.get(id=profile_id)
            analysis, created = Analysis.objects.get_or_create(
                profile=profile,
                analysis_type='activity',
                defaults={
                    'result': {
                        'total_posts': 150,
                        'avg_posts_per_day': 0.5,
                        'peak_activity_hour': 20,
                        'engagement_rate': 4.5
                    },
                    'confidence_score': 0.92
                }
            )
            serializer = AnalysisSerializer(analysis)
            return Response(serializer.data)
        except Profile.DoesNotExist:
            return Response(
                {'error': 'Profile not found'},
                status=status.HTTP_404_NOT_FOUND
            )
