from django.views.generic import ListView , CreateView
from django.urls import reverse_lazy
from .forms import StaffForm
from .models import Staff

class StaffListView(ListView):
    model = Staff
    form_class = StaffForm
    template_name = 'staff_list.html'
    context_object_name = 'staff_members'
class AddStaffView(CreateView):
    model = Staff
    form_class = StaffForm
    template_name = 'add_staff.html'
    success_url = reverse_lazy('staff_list')