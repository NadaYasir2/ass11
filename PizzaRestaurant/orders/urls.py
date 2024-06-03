from django.urls import path
from .import views

urlpatterns = [
    path('', views.WelcomeView.as_view(), name='welcome'),
    path('homepage/', views.HomepageView.as_view(), name='homepage'),
    path('menu/', views.MenuView.as_view(), name='menu'),
    path('order/', views.OrderPizzaView.as_view(), name='order_pizza'),
]
