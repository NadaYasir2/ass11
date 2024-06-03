from django.views.generic import ListView
from .models import Staff

class StaffListView(ListView):
    model = Staff
    template_name = 'staff/staff_list.html'
    context_object_name = 'staff_members'
