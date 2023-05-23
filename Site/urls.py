from django.urls import path
from Site import views

urlpatterns = [
    path('', views.index, name ='index'),
    path ('produtos', views.produto_lista, name='produto_lista'),
    path('produto', views.produto_detalhe, name='produto_detalhe'),
    path('sobre-a-empresa', views.institucional, name='institucional'),
    path('contatos', views.contatos, name='fale_conosco'),
    path('cadastro', views.cadastro, name='cadastros')
]