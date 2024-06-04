from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy
from .models import Pizza, Order
from .forms import OrderForm

class HomepageView(TemplateView):
    template_name = 'orders/homepage.html'
    context_object_name = 'pizzas'
    paginate_by = 5

class WelcomeView(TemplateView):
    template_name = 'orders/welcome.html'

class MenuView(ListView):
    model = Pizza
    template_name = 'orders/menu.html'
    context_object_name = 'pizzas'
    def get_queryset(self):
        return Pizza.objects.all().order_by('name')

class OrderPizzaView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'orders/order_pizza.html'
    success_url = reverse_lazy('menu')

    def form_valid(self, form):
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pizzas'] = Pizza.objects.all().order_by('name')
        return context