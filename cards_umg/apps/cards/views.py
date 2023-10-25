import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from django.db.models import Q
from django.contrib import messages  # Importa el módulo messages
from apps.core.models import Categoria
from .models import Collection, Card


def list_collections(request):
    collections = Collection.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'colecciones/list-collections.html', {'colecciones': collections, 'categorias': categorias})


def list_filter_collections(request):
    search_query = request.GET.get('search', '')  # Obtener el parámetro de búsqueda desde la URL
    collections = Collection.objects.filter(Q(nombre__icontains=search_query) | Q(descripcion__icontains=search_query))
    categorias = Categoria.objects.all()
    return render(request, 'colecciones/list-collections.html', {'colecciones': collections, 'categorias': categorias, 'search_query': search_query})


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
    return redirect('cards:list-collections')


def create_card(request):
    if request.method == 'POST':
        enunciado = request.POST.get('enunciado')
        respuesta = request.POST.get('respuesta')
        coleccion_id = request.POST.get('coleccion_id')  # Asume que se envía el ID de la colección a la que pertenece
        
        try:
            coleccion = get_object_or_404(Collection, pk=coleccion_id)
            card = Card(enunciado=enunciado, respuesta=respuesta, coleccion=coleccion)
            card.save()
            messages.success(request, 'Tarjeta creada exitosamente.')
            return redirect('cards:list-cards-in-collection', collection_id=coleccion_id)
        except Collection.DoesNotExist:
            messages.error(request, 'La colección no existe')
            return redirect('cards:list-collections')
        except Exception as e:
            messages.error(request, f'Error al crear la tarjeta: {str(e)}')
            return redirect('cards:list-cards-in-collection', collection_id=coleccion_id)
    else:
        return redirect('cards:list-collections')

def list_cards_in_collection(request, collection_id):
    # Obtener la colección correspondiente o mostrar un error si no existe
    collection = get_object_or_404(Collection, pk=collection_id)
    
    # Filtrar las tarjetas que pertenecen a esta colección
    cards = Card.objects.filter(coleccion=collection)
    
    return render(request, 'cards/cards_collection.html', {'collection': collection, 'cards': cards})


def update_card(request, card_id):
    card = get_object_or_404(Card, pk=card_id)
    
    if request.method == 'POST':
        enunciado = request.POST.get('enunciado')
        respuesta = request.POST.get('respuesta')
        coleccion_id = request.POST.get('coleccion_id')  # Asume que se envía el ID de la colección a la que pertenece
        
        try:
            coleccion = get_object_or_404(Collection, pk=coleccion_id)
            card.enunciado = enunciado
            card.respuesta = respuesta
            card.coleccion = coleccion
            card.save()
            messages.success(request, 'Tarjeta actualizada exitosamente.')
            return redirect('cards:list-cards')
        except Collection.DoesNotExist:
            messages.error(request, 'La colección no existe')
            return redirect('cards:list-cards')
        except Exception as e:
            messages.error(request, f'Error al actualizar la tarjeta: {str(e)}')
            return redirect('cards:list-cards')
    
    return render(request, 'cards/update_card.html', {'card': card})

def delete_card(request, card_id):
    card = get_object_or_404(Card, pk=card_id)
    collection_id = card.coleccion.id
    card.delete()
    messages.success(request, 'Tarjeta eliminada exitosamente.')
    return redirect('cards:list-cards-in-collection', collection_id=collection_id)