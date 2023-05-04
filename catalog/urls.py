from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    path('catalogo',views.catalogo, name='catalogo'),
    path('crear/', views.crear_producto, name='crear_producto'),
    path('<int:producto_id>/', views.ver_producto, name='ver_producto'),
    path('<int:producto_id>/eliminar/', views.eliminar_producto, name='eliminar_producto'),
    path('<int:producto_id>/editar/', views.editar_producto, name='editar_producto'),
]
