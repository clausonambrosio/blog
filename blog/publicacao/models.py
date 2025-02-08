from django.db import models
from django.utils import timezone

class Postagem(models.Model):  
    titulo = models.CharField(max_length=100)  
    conteudo = models.CharField(max_length=1000)  
    data_publicacao = models.DateTimeField(auto_now_add=True)
