from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from .models import Producto
from .form import CatalogoForm

# Funcion de catalogo
def catalogo(request):
    productos = Producto.objects.all()
    search_term = request.GET.get('search')
    if search_term:
        productos = productos.filter(nombre__icontains=search_term)
    return render(request, 'catalogo.html', {'productos': productos})

# Funcion para ver el producto creado por id
def ver_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request, 'ver_producto.html', {'producto': producto})

# Funcion para crear el producto mediante formulario
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
    
# Funcion para eliminar un producto
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('productos:catalogo')
    return render(request, 'eliminar_producto.html', {'producto': producto})

# Función para editar un producto
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    if request.method == 'POST':
        form = CatalogoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('productos:ver_producto', producto_id=producto.id)
    else:
        form = CatalogoForm(instance=producto)
    return render(request, 'editar_producto.html', {'form': form})






