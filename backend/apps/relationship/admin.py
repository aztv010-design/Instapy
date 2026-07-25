from django.contrib import admin
from .models import Relationship

@admin.register(Relationship)
class RelationshipAdmin(admin.ModelAdmin):
    list_display = ('source_profile', 'relationship_type', 'target_profile', 'created_at')
    list_filter = ('relationship_type', 'created_at')
    search_fields = ('source_profile__username', 'target_profile__username')
    readonly_fields = ('created_at',)
