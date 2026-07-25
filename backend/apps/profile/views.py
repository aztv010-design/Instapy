from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Profile
from .serializers import ProfileSerializer
from django.utils import timezone

class ScanProfileView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        username = request.data.get('username')
        
        if not username:
            return Response(
                {'error': 'Username is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        profile, created = Profile.objects.get_or_create(
            username=username,
            defaults={'full_name': username}
        )
        
        # Update last scanned time
        profile.last_scanned = timezone.now()
        profile.save()
        
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ProfileDetailView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, username):
        try:
            profile = Profile.objects.get(username=username)
            serializer = ProfileSerializer(profile)
            return Response(serializer.data)
        except Profile.DoesNotExist:
            return Response(
                {'error': 'Profile not found'},
                status=status.HTTP_404_NOT_FOUND
            )
