from django.contrib import admin
from .models import Geolocation

@admin.register(Geolocation)
class GeolocationAdmin(admin.ModelAdmin):
    list_display = ('profile', 'city', 'country', 'created_at')
    list_filter = ('country', 'created_at')
    search_fields = ('profile__username', 'city', 'country')
    readonly_fields = ('created_at', 'updated_at')
