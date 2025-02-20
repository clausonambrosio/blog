from django.db import models
from django.utils import timezone

class Pessoa(models.Model):  
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    endereco = models.CharField(max_length=1000)
    data_nascimento = models.DateField()
    url_portfolio = models.URLField(blank=True, null=True)
    imagem = models.ImageField(upload_to='pessoas/', blank=True, null=True)
    


