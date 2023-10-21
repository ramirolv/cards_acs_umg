from django.contrib import admin
from django.urls import path, include
from .views import *

app_name='cards'

urlpatterns = [
    #Collections
    path('collections/', list_collections, name='list-collections'),
    path('collections/create/', create_collection, name='create-collection'),
    path('collections/by_categoria/<int:pk>', listar_colecciones_por_categoria, name='list-collection-by-categorias'),
    path('collections/update/<int:pk>/', update_collection, name='update-collection'),
    path('collections/delete/<int:pk>/', delete_collection, name='delete-collection'),

    #Cards
    path('collections/cards/<int:collection_id>/', list_cards_in_collection, name='list-cards-in-collection'),
    path('cards/crear/', create_card, name='create-card'),
    path('cards/editar/<int:card_id>/', update_card, name='update-card'),
    path('cards/eliminar/<int:card_id>/', delete_card, name='delete-card'),
]