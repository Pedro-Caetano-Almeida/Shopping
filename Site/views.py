from django.shortcuts import render
from Site.forms import ClienteForm, ContatoForm
from Site.models import Departamento, Produto, Cliente
from django.core.mail import send_mail

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
    mensagem = ""
    if request.method == "POST":
        nome = request.POST['nome']
        telefone = request.POST['telefone']
        assunto = request.POST['assunto']
        mensagem = request.POST['mensagem']
        remetente = request.POST['email']
        destinatario = ['profronicosta@gmail.com']
        corpo = f"Nome: {nome} \nE=mail: {remetente} \nTelefone: {telefone}  \nMensagem: {mensagem}"
    
        try:
            send_mail(assunto, corpo, remetente, destinatario )
            mensagem = 'E-mail enviado com sucesso!'
        except:
            mensagem = 'Erro ao enviar e-mail!'
    formulario = ContatoForm()

    context = {
        'form_contato' : formulario,
        'mensagem' : mensagem
    }
    return render(request, 'contato.html', context)

def cadastro(request):
    mensagem = ""
    #quando envio o formulário preenchido
    if request.method == "POST":
        formulario = ClienteForm(request.POST)
        if formulario.is_valid():
            cliente = formulario.save()
            formulario = ClienteForm()
            mensagem = "Cliente cadastrado com sucesso"
    #quando entro na tela vazia
    else:
        formulario = ClienteForm()

    context = {
        'form_cliente': formulario,  
        'mensagem': mensagem
    }
    return render(request, 'cadastro.html', context)

