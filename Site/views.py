from django.shortcuts import render

from Site.models import Departamento, Produto

# Create your views here.
def index(request):
    return render(request,'index.html')


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
    return render(request,'produto_detalhes.html')

def institucional(request):
    return render(request, 'empresa.html')

def contatos(request):
    return render(request, 'contato.html')

def cadastro(request):
    return render(request, 'cadastro.html')