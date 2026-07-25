from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'full_name', 'followers', 'verified', 'created_at')
    list_filter = ('verified', 'is_private', 'created_at')
    search_fields = ('username', 'full_name', 'email')
    readonly_fields = ('created_at', 'updated_at', 'last_scanned')
    fieldsets = (
        ('Basic Info', {'fields': ('username', 'full_name', 'bio')}),
        ('Stats', {'fields': ('followers', 'following', 'posts')}),
        ('Details', {'fields': ('verified', 'is_private', 'website', 'email', 'phone')}),
        ('Media', {'fields': ('profile_pic_url',)}),
        ('Dates', {'fields': ('last_scanned', 'created_at', 'updated_at')}),
    )
