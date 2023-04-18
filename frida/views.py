from django.shortcuts import render
from django.views import generic
from .models import Review


class ReviewList(generic.ListView):
    model = Review
    template_name = "base.html"
    paginate_by = 3


def home_page(request):
    return render((request), 'base.html')


def menu_page(request):
    return render((request), 'menu.html')


def gallery_page(request):
    return render((request), 'gallery.html')


def book_page(request):
    return render((request), 'book.html')


def account_page(request):
    return render((request), 'account.html')
