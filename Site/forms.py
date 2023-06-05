from django import forms
from Site.models import Cliente

class ClienteForm( forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


class ContatoForm(forms.Form):
    nome = forms.CharField()
    email = forms.CharField()
    telefone = forms.CharField()
    assunto = forms.CharField()
    mensagem = forms.CharField()

    class Meta:
        widgets = {
            'telefone': forms.TextInput(attrs={'class':'phone_with_ddd'}),
            'mensagem': forms.Textarea
        }

