from django.shortcuts import redirect, render
from .models import Producto
from .form import CatalogoForm

def catalogo(request):

    return render(request, 'index.html')


def crear_producto(request):
    if request.method == 'POST':
        form = CatalogoForm(request.POST)
        if form.is_valid():
            Producto = form.save(commit=False)
            # Asigna el usuario actual como creador del producto
            Producto.creador = request.user
            Producto.save()
            return redirect('Producto:catalogo')
    else:
        form = CatalogoForm()
    return render(request, 'crear_producto.html', {'form': form})
