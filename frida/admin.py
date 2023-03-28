from django.contrib import admin
from .models import Review
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(approved=True)
