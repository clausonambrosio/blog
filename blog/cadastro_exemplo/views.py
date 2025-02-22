from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Pessoa, Habilidade

class PessoaListView(ListView):
    model = Pessoa
    template_name = 'cadastro_exemplo/lista.html'
    context_object_name = 'pessoas'
    paginate_by = 100

class PessoaDetailView(DetailView):
    model = Pessoa
    template_name = 'cadastro_exemplo/detalhe.html'

class PessoaCreateView(CreateView):
    model = Pessoa
    template_name = 'cadastro_exemplo/form.html'
    fields = ['nome', 'sobrenome', 'data_aniversario', 'url_portfolio', 'imagem', 'habilidades']
    success_url = reverse_lazy('lista_pessoas')

class PessoaUpdateView(UpdateView):
    model = Pessoa
    template_name = 'cadastro_exemplo/form.html'
    fields = ['nome', 'sobrenome', 'data_aniversario', 'url_portfolio', 'imagem', 'habilidades']

class PessoaDeleteView(DeleteView):
    model = Pessoa
    template_name = 'cadastro_exemplo/confirmar_exclusao.html'
    success_url = '/cadastro_exemplo/'

# View para buscar pessoas
def buscar_pessoa(request):
    if request.method == 'GET':
        termo = request.GET.get('q')
        pessoas = Pessoa.objects.filter(nome__icontains=termo)
        return render(request, 'cadastro_exemplo/lista.html', {'pessoas': pessoas})


class HabilidadeCreateView(CreateView):
    model = Habilidade
    template_name = 'habilidades/form.html'
    fields = ['nome', 'descricao']
    success_url = reverse_lazy('lista_pessoas')