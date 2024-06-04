from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView

class CustomLoginView(LoginView):
    template_name = 'login.html'
    next_page = reverse_lazy('homepage')



class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('homepage')
    http_method_names = ["get", "post"]

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        return response