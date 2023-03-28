from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Review(models.Model):

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviews"
    )
    email = models.EmailField()
    content = models.TextField()
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title
