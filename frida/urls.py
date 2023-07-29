from frida.views import add_review, add_booking
from . import views
from django.urls import path, include
from frida.views import home_page, ReviewList, menu_page, gallery_page, book_page, account_page


urlpatterns = [
    path('', home_page, name='home'),
    path('reviews/', views.ReviewList.as_view(), name='review-list'),
    path('menu/', menu_page, name='menu'),
    path('gallery/', gallery_page, name='gallery'),
    path('book/', book_page, name='book'),
    path('account/', account_page, name='account'),
    path('add_review/', views.add_review, name='add_review'),
    path('add_booking/', views.add_booking, name='add_booking'),
]
