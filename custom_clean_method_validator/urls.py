from django.urls import path
from .views import employee_view


urlpatterns = [
    path('ev/', employee_view)
]

