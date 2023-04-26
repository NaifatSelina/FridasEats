from django.shortcuts import render, redirect
from django.views import generic
from .models import Review
from .forms import ReviewForm


class ReviewList(generic.ListView):
    model = Review
    template_name = "base.html"
    paginate_by = 3, {
       "review_form": ReviewForm()
    }


def post():

    review_form = ReviewForm(data=request.POST)

    if review_form.is_valid():
        review_form.instance.email = request.user.email
        review_form.instance.name = request.user.author
        review = review_form.save(commit=False)
        review.post = post
        review.save()
    else:
        review_form = ReviewForm()


def home_page(request):
    # return render((request), 'base.html')
    return render((request), 'base.html', {"review_form": ReviewForm()})


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
        review_form = ReviewForm(data=request.POST)

        review_form.save()
        return redirect('home')

    return render(request, 'base.html')

