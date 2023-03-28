from django.shortcuts import render
from django.views import generic
from .models import Review


class ReviewList(generic.ListView):
    model = Review
    queryset = Post.objects.filter(status=1).order_by("-author")
    template_name = "index.html"
    paginate_by = 3


def home_page(request):
    return render((request), 'frida/index.html')
