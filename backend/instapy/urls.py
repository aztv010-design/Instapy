from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

# API Router
router = DefaultRouter()

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    
    # API Authentication
    path('api/auth/token/', obtain_auth_token, name='api_token_auth'),
    
    # API Schema & Documentation
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    
    # API Endpoints
    path('api/', include(router.urls)),
    path('api/profile/', include('apps.profile.urls')),
    path('api/analysis/', include('apps.analysis.urls')),
    path('api/geolocation/', include('apps.geolocation.urls')),
    path('api/relationship/', include('apps.relationship.urls')),
    path('api/reports/', include('apps.reports.urls')),
    path('api/users/', include('apps.users.urls')),
]

# Serve media and static files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
