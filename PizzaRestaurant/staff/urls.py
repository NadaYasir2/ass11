from django.urls import path
from . import views

urlpatterns = [
    path('', views.StaffListView.as_view(), name='staff_list'),
]
