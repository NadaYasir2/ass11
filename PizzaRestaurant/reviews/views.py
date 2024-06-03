from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Review
from .forms import ReviewForm

class ReviewListView(ListView):
    model = Review
    template_name = 'reviews_list.html'
    context_object_name = 'reviews'

class AddReviewView(CreateView):
    model = Review
    template_name = 'add_review.html'
    success_url = reverse_lazy('review_list')
