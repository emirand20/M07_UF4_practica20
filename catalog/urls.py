from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    path('',views.catalogo, name='prueba'),
    path('crear/', views.crear_producto, name='crear_producto'),
     path('<int:producto_id>/', views.ver_producto, name='ver_producto'),
]
