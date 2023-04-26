from django.shortcuts import render
from django.views import generic
from .models import Review
from .forms import ReviewForm


class ReviewList(generic.ListView):
    model = Review
    template_name = "base.html"
    paginate_by = 3, {
       "review_form": ReviewForm()
    }


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


def add_review(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        rating = request.POST.get('rating')
        comments = request.POST.get('comments')

        review = Review(name=name, email=email, rating=rating, comments=comments)
        review.save()

        return redirect('')

    return render(request, 'base.html')
