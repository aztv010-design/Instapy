from django.urls import path
from . import views

urlpatterns = [
    path('scan/', views.ScanProfileView.as_view(), name='scan-profile'),
    path('<str:username>/', views.ProfileDetailView.as_view(), name='profile-detail'),
]
