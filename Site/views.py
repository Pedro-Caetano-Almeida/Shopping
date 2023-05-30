from django.shortcuts import render
from Site.forms import ClienteForm

from Site.models import Departamento, Produto

# Create your views here.
def index(request):
    produtos_em_destaque = Produto.objects.filter(destaque = True)
    context = {
        'produtos': produtos_em_destaque
    }
    return render(request,'index.html', context)


def produto_lista(request):
    produtos = Produto.objects.all()
    context = {
        'produtos': produtos,
        'nome_categoria': "Todos Produtos"
    }
    return render(request,'produtos.html', context)


def produto_lista_por_id(request, id):
    departamentos = Departamento.objects.all()
    produtos_por_departamento = Produto.objects.filter(departamento_id = id)
    categoria = departamentos.get(id = id).nome
    context = {
        'departamentos': departamentos,
        'produtos': produtos_por_departamento,
        'nome_categoria': categoria 
    }
    return render(request,'produtos.html', context)

def produto_detalhe(request, id):
    produto = Produto.objects.get(id = id)  #aqui é melhor usar get doq filter pq filter retorna uma lista e get pega um só
    produtos_relacionados = Produto.objects.filter(departamento_id = produto.departamento.id)[:4] #aqui é para pegar só 4 itens!!
    context = {
        'produto': produto,
        'produtos_relacionados': produtos_relacionados
    }
    return render(request,'produto_detalhes.html', context)

def institucional(request):
    return render(request, 'empresa.html')

def contatos(request):
    return render(request, 'contato.html')

def cadastro(request):
    if request.method == "POST":
        formulario = ClienteForm(request.POST)
        if formulario.is_valid():
            cliente = formulario.save()
            formulario = ClienteForm()
    else: 
        formulario = ClienteForm()
    context = {
        'form_cliente': formulario
    }
    return render(request, 'cadastro.html', context)