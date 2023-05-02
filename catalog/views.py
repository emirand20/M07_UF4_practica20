from django.shortcuts import redirect, render, get_object_or_404
from .models import Producto
from .form import CatalogoForm

def catalogo(request):
    productos = Producto.objects.all()
    return render(request, 'index.html', {'productos': productos})

def ver_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request, 'ver_producto.html', {'producto': producto})

def crear_producto(request):
    if request.method == 'POST':
        form = CatalogoForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.creador = request.user
            producto.save()
            return redirect('productos:ver_producto', producto_id=producto.id)
    else:
        form = CatalogoForm()
    return render(request, 'crear_producto.html', {'form': form})
