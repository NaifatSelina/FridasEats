from .models import Review, Booking
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('author', 'email', 'rating', 'content',)


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('full_name', 'email', 'phone_number', 'date', 'time')
