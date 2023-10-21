from django.contrib import admin
from django.urls import path, include
from .views import *

app_name='cards'

urlpatterns = [
    path('collections/', list_collections, name='list-collections'),
    path('collections/create/', create_collection, name='create-collection'),
    path('collections/by_categoria/<int:pk>', listar_colecciones_por_categoria, name='list-collection-by-categorias'),
    path('collections/update/<int:pk>/', update_collection, name='update-collection'),
    path('collections/delete/<int:pk>/', delete_collection, name='delete-collection'),
]