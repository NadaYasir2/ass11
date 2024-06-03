from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('orders.urls')),
    path('reviews/', include('reviews.urls')),
    path('staff/', include('staff.urls')),
    path('accounts/', include('accounts.urls')),
]
