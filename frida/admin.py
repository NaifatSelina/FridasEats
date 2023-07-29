from django.contrib import admin
from .models import Review
from .models import Booking


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = ('author', 'email', 'approved')
    list_filter = ('approved', 'rating', 'author')
    search_fields = ('author', 'email', 'rating')
    actions = ['approve_bookings']

    def approve_reviews(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'date', 'time', 'approved')
    list_filter = ('approved', 'date')
    search_fields = ('full_name', 'email', 'phone_number', 'date')
    actions = ['approve_bookings']

    def approve_bookings(self, request, queryset):
        queryset.update(approved=True)
