from django.urls import path
from . import views

urlpatterns = [
    path('carrito', views.tienda, name='tienda'),
]