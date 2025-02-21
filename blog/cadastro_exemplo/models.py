from django.db import models

# Create your models here.


from django.db import models
from django.urls import reverse
from django.utils.timezone import now

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    data_aniversario = models.DateField()
    url_portfolio = models.URLField(blank=True, null=True)
    imagem = models.ImageField(upload_to='pessoas/', blank=True, null=True)
    
    # Campos calculados/automáticos (não precisam ser preenchidos)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    # Relacionamentos
    habilidades = models.ManyToManyField('Habilidade', blank=True)

    @property
    def idade(self):
        return (now().date() - self.data_aniversario).days // 365

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"

    def get_absolute_url(self):
        return reverse('detalhe_pessoa', args=[str(self.id)])

# Modelo adicional para habilidades
class Habilidade(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome