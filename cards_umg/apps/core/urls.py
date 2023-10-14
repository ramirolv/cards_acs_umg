from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import *

app_name='core'

urlpatterns = [
    path('', home_view, name='home'),
    path('categorias/', categorias_view, name='categorias'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)