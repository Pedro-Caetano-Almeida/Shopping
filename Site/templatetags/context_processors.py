from Site.models import Departamento

def departamentos(request):
    return {'departamentos': Departamento.objects.all()} #aqui estamos criando uma variável que vai pegar todos os departamentos que está no model
 