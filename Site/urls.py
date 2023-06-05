from django.urls import path
from Site import views

urlpatterns = [
    path('', views.index, name ='index'),
    path ('produtos', views.produto_lista, name='produto_lista'),
    path('produto', views.produto_detalhe, name='produto_detalhe'),
    path('sobre-a-empresa', views.institucional, name='institucional'),
    path('contatos', views.contatos, name='contato'),
    path('cadastro', views.cadastro, name='cadastros'),
    path('produtos/<int:id>', views.produto_lista_por_id, name= 'produto_lista_por_id'),
    path('produto/<int:id>', views.produto_detalhe, name='produto_detalhe'), #aqui usamos o mesmo do produto pq o produto sempre vai precisar de id

]