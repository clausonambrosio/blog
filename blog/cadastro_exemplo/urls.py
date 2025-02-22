from django.urls import path
from . import views

urlpatterns = [
    path('', views.PessoaListView.as_view(), name='lista_pessoas'),
    path('pessoas/<int:pk>/', views.PessoaDetailView.as_view(), name='detalhe_pessoa'),
    path('pessoas/criar/', views.PessoaCreateView.as_view(), name='criar_pessoa'),
    path('pessoas/<int:pk>/editar/', views.PessoaUpdateView.as_view(), name='editar_pessoa'),
    path('pessoas/<int:pk>/excluir/', views.PessoaDeleteView.as_view(), name='excluir_pessoa'),
    path('buscar/', views.buscar_pessoa, name='buscar_pessoa'),
    path('habilidades/criar/', views.HabilidadeCreateView.as_view(), name='criar_habilidade'),

]