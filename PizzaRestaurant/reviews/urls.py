from django.urls import path
from .views import ReviewListView, AddReviewView

urlpatterns = [
    path('', ReviewListView.as_view(), name='review_list'),
    path('add/', AddReviewView.as_view(), name='add_review'),
]
