from . import views
from django.urls import path


urlpatterns = [
    path('', views.ReviewList.as_view(), name='review-list'),
]
