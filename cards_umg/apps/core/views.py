from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import *

# Create your views here.


def home_view(request):
    return render(request, 'index.html')


def categorias_view(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias/listar-categoria.html', {'categorias': categorias})


def create_categoria(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        icono = request.FILES.get('icono')

        try:
            Categoria.objects.create(nombre=nombre, icono=icono)
            messages.success(request, 'Categoría creada exitosamente.')
        except Exception as e:
            messages.error(request, f'Error al crear la categoría: {str(e)}')

    return redirect('core:categorias')


def update_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        icono = request.FILES.get('icono')

        try:
            categoria.nombre = nombre
            if icono:
                categoria.icono = icono
            categoria.save()
            messages.success(request, 'Categoría actualizada exitosamente.')
        except Exception as e:
            messages.error(
                request, f'Error al actualizar la categoría: {str(e)}')

    return redirect('core:categorias')


def delete_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)

    try:
        categoria.delete()
        messages.success(request, 'Categoría eliminada exitosamente.')
    except Exception as e:
        messages.error(request, f'Error al eliminar la categoría: {str(e)}')

    return redirect('core:categorias')


def nosotros_view(request):
    return render(request, 'nosotros/nosotros.html')