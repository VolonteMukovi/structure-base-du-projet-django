from django.urls import path
from .views import utilisateurs_view

urlpatterns = [
    path('utilisateurs/', utilisateurs_view)
]