from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReviewListView.as_view(), name='review_list'),
    path('add/', views.AddReviewView.as_view(), name='add_review'),
]
