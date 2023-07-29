from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MaxValueValidator, MinValueValidator

STATUS = ((0, "Draft"), (1, "Published"))

RATING_CHOICES = [(1, '1 star'),    (2, '2 stars'),    (3, '3 stars'),    (4, '4 stars'),    (5, '5 stars'),]


class Review(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviews"
    )
    email = models.EmailField()
    content = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], default=0)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["author"]

    def __str__(self):
        return f"A review was submitted by {self.author}."


class Booking(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Booking by {self.full_name}"
