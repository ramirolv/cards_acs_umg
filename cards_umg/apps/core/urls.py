from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import *

app_name='core'

urlpatterns = [
    path('', home_view, name='home'),
    path('categorias/', categorias_view, name='categorias'),
    path('categorias/create/', create_categoria, name='create-categoria'),
    path('categorias/update/<int:pk>/', update_categoria, name='update-categoria'),
    path('categorias/delete/<int:pk>/', delete_categoria, name='delete-categoria'),
    
    path('nosotros/', nosotros_view, name='nosotros'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)