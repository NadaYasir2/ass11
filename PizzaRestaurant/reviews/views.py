from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Review
from .forms import ReviewForm
from django.contrib import messages

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

    def submit_review(request):
        if request.method == 'POST':
            # Handle the form submission logic
            review_text = request.POST.get('review_text')
            rating = request.POST.get('rating')

            # Save the review (assuming you have a Review model)
            Review.objects.create(
                user=request.user,
                text=review_text,
                rating=rating,
            )

            # Add a success message
            messages.success(request, 'Success! Your review has been successfully submitted.')

            return redirect('add_review')  # Redirect to the same page or another page

        return render(request, 'add_review.html')