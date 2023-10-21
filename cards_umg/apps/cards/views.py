from django.shortcuts import render

# Create your views here.
# Vistas
from django.shortcuts import render, redirect, get_object_or_404
from .models import Collection
from django.http import HttpResponse
from django.core import serializers
import json

def list_collections(request):
    collections = Collection.objects.all()
    return render(request, 'collection/list.html', {'collections': collections})

def create_collection(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            nombre = data['nombre']
            descripcion = data['descripcion']
            # Asume que categoria es un campo clave externa
            # categoria_id = data['categoria']
            # categoria = Categoria.objects.get(pk=categoria_id)
            collection = Collection(nombre=nombre, descripcion=descripcion)
            collection.save()
            return redirect('list-collections')
        except KeyError:
            return HttpResponse('Invalid data provided', status=400)
        
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
