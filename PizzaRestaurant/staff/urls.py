from django.urls import path
from . import views

urlpatterns = [
    path('', views.StaffListView.as_view(), name='staff_list'),
    path('add/', views.AddStaffView.as_view(), name='add_staff'),
]

