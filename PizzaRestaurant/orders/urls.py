from django.urls import path
from .views import WelcomeView, MenuView, OrderPizzaView

urlpatterns = [
    path('', WelcomeView.as_view(), name='welcome'),
    path('menu/', MenuView.as_view(), name='menu'),
    path('order/', OrderPizzaView.as_view(), name='order_pizza'),
]
