from django.contrib import admin
from django.urls import path, include
from .views import *

app_name='core'

urlpatterns = [
    path('', home_view, name='nueva'),
    path('categorias/', categorias_view, name='categorias'),
]