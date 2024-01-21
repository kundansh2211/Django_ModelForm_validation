from django.urls import path
from .views import user_view

urlpatterns = [
    path('uv/', user_view)
]
