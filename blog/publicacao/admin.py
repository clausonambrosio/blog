from django.contrib import admin

from .models import Postagem  

@admin.register(Postagem)  
class PostagemAdmin(admin.ModelAdmin):  
    list_display = ['titulo', 'conteudo', 'data_publicacao']  
    search_fields = ['nome']