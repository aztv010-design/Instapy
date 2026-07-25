from django.contrib import admin
from .models import Report

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('profile', 'title', 'format', 'created_at')
    list_filter = ('format', 'created_at')
    search_fields = ('profile__username', 'title')
    readonly_fields = ('created_at',)
