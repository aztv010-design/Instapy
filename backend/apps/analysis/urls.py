from django.urls import path
from . import views

urlpatterns = [
    path('fake-detection/<int:profile_id>/', views.FakeDetectionView.as_view(), name='fake-detection'),
    path('activity/<int:profile_id>/', views.ActivityAnalysisView.as_view(), name='activity-analysis'),
]
