from django.shortcuts import render
from django.http import HttpResponse
from .models import Postagem  

# Create your views here.

def lista_postagens(request):  
    postagens = Postagem.objects.all()  
    return render(request, 'lista.html', {'postagens': postagens})