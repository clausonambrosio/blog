from django.shortcuts import render
from .models import Postagem  

# Create your views here.

def lista_postagens(request):  
    postagens = Postagem.objects.all()  
    return render(request, 'postagens/lista.html', {'postagens': postagens})