from django import forms
from Site.models import Cliente

class ClienteForm( forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'cpf':forms.TextInput(attrs={'class':'cpf'}),
            'data_nascimento': forms.TextInput(attrs={'class':'date'}),
            'cep': forms.TextInput(attrs={'classe':'cep'}),
        }


class ContatoForm(forms.Form):
    nome = forms.CharField()
    email = forms.CharField()
    telefone = forms.CharField(widget=forms.TextInput(attrs={'class':'phone_with_ddd'}))
    assunto = forms.CharField()
    mensagem = forms.CharField(widget=forms.Textarea)


