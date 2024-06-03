from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy
from .models import Pizza, Order
from .forms import OrderForm

class WelcomeView(TemplateView):
    template_name = 'orders/welcome.html'

class MenuView(ListView):
    model = Pizza
    template_name = 'orders/menu.html'
    context_object_name = 'pizzas'

class OrderPizzaView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'orders/order_pizza.html'
    success_url = reverse_lazy('welcome')
