from django.shortcuts import render, redirect
from django.views import generic
from .models import Review, Booking
from .forms import ReviewForm, BookingForm

# only 3 reviews can appear on page


class ReviewList(generic.ListView):
    model = Review
    template_name = "base.html"
    paginate_by = 3, {
       "review_form": ReviewForm(),
    }


class BookingList(generic.ListView):
    model = Booking
    template_name = "base.html"
    paginate_by = 3, {
       "booking_form": BookingForm()
    }

# displays each webpage


def home_page(request):
    return render((request), 'base.html', {"review_form": ReviewForm()})


def menu_page(request):
    return render((request), 'menu.html')


def gallery_page(request):
    return render((request), 'gallery.html')


def book_page(request):
    return render((request), 'book.html')


def account_page(request):
    return render((request), 'account.html')

# review and booking forms


def add_review(request):
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.author = request.user  # Using 'request.user' to link the currently logged-in user.
            review.save()
            return redirect('home')
    else:
        review_form = ReviewForm()

    return render(request, 'base.html', {"review_form": review_form})


def add_booking(request):
    if request.method == 'POST':
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            booking = booking_form.save()
            booking.save()
            return redirect('home')
    else:
        booking_form = BookingForm()

    return render(request, 'base.html', {"booking_form": booking_form})
