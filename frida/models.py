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
        return f"This review was submitted by {self.author}."
