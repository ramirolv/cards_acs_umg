from django.shortcuts import render
from .models import *

# Create your views here.
def home_view(request):
    return render(request, 'index.html')

def categorias_view(request):
    categorias = Categoria.objects.all()
    return render(request,'categorias/listar-categoria.html',{'categorias':categorias})