from django.contrib import admin
from .models import Pessoa  

@admin.register(Pessoa)  
class PessoaAdmin(admin.ModelAdmin):  
    list_display = ['nome', 'sobrenome', 'email', 'endereco', 'data_nascimento']  
    search_fields = ['nome']