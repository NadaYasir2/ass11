from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Review
from .forms import ReviewForm

class ReviewListView(ListView):
    model = Review
    template_name = 'review_list.html'
    success_url = reverse_lazy('homepage')
    context_object_name = 'reviews'

class AddReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'add_review.html'
    success_url = reverse_lazy('review_list')
