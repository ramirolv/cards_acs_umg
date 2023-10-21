import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from django.contrib import messages  # Importa el módulo messages
from apps.core.models import Categoria
from .models import Collection


def list_collections(request):
    collections = Collection.objects.all()
    return render(request, 'colecciones/list-collections.html', {'colecciones': collections})


def listar_colecciones_por_categoria(request, pk):
    try:
        categorias = Categoria.objects.all()
        categoria = categorias.get(pk=pk)
        colecciones = Collection.objects.filter(categoria=categoria)

        return render(request, 'colecciones/list-collections.html', {'categoria': categoria, 'categorias': categorias, 'colecciones': colecciones})

    except categoria.DoesNotExist:
        # Manejo de error si la categoría no existe
        messages.error(request, 'La categoría no existe')
        return redirect('core:categorias')

    except Exception as e:
        # Manejo de otros errores
        print(e)
        messages.error(request, f'Error: {str(e)}')
        return redirect('core:categorias')


def create_collection(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        categoria_id = request.POST.get('categoria')
        miniatura = request.FILES.get('miniatura')  # Obtén el archivo de miniatura

        try:
            categoria = Categoria.objects.get(pk=categoria_id)
            collection = Collection(
                nombre=nombre, descripcion=descripcion, categoria=categoria, miniatura=miniatura)
            collection.save()
            messages.success(request, 'Colección creada exitosamente.')
            return redirect('cards:list-collections')
        except Categoria.DoesNotExist:
            messages.error(request, 'La categoría no existe')
        except Exception as e:
            messages.error(request, f'Error al crear la colección: {str(e)}')

    return redirect('cards:list-collections')



def update_collection(request, pk):
    collection = get_object_or_404(Collection, pk=pk)

    if request.method == 'PUT':
        data = json.loads(request.body)
        try:
            collection.nombre = data['nombre']
            collection.descripcion = data['descripcion']
            collection.save()
            return HttpResponse('Collection updated successfully')
        except KeyError:
            return HttpResponse('Invalid data provided', status=400)


def delete_collection(request, pk):
    collection = get_object_or_404(Collection, pk=pk)
    collection.delete()
    return redirect('list-collections')
