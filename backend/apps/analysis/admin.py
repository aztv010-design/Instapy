from django.contrib import admin
from .models import Analysis, FakeDetectionResult

@admin.register(Analysis)
class AnalysisAdmin(admin.ModelAdmin):
    list_display = ('profile', 'analysis_type', 'confidence_score', 'created_at')
    list_filter = ('analysis_type', 'created_at')
    search_fields = ('profile__username',)
    readonly_fields = ('created_at',)

@admin.register(FakeDetectionResult)
class FakeDetectionAdmin(admin.ModelAdmin):
    list_display = ('profile', 'is_fake', 'confidence', 'created_at')
    list_filter = ('is_fake', 'created_at')
    search_fields = ('profile__username',)
    readonly_fields = ('created_at',)
