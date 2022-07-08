
import email
import json
from wsgiref.util import request_uri
from .models import Funcionario, Pessoa
from .serializers import FuncionarioSerializer, PessoaSerializer


# Create your views here.
from django.http import JsonResponse

def health(request):
    return JsonResponse({"mensagem": 'ok'}, safe=False)
 

def Funcionarios(request):
    '''View Funcionário'''

    query_params = request.GET 

    if request.method == 'GET':

        qtd_funcionarios = Funcionario.objects.all().values()
        all_serializer = FuncionarioSerializer(qtd_funcionarios, many=True)
        return JsonResponse({'todos': all_serializer.data})

    if request.method == 'POST':
        
        data = json.loads(request.body)
        funcionario = Funcionario()
        funcionario.nome = data.get('nome')
        funcionario.sobrenome = data.get('sobrenome')
        funcionario.funcao = data.get('funcao')
        funcionario.email = data.get('email')
        funcionario.ano_nascimento = data.get('ano_nascimento')

        lista_qtd_funcio = Funcionario.objects.filter(email=funcionario.email).count()
        lista_qtd_funcio_nome = Funcionario.objects.filter(nome=funcionario.nome).count()

        if lista_qtd_funcio > 0:
            return JsonResponse({'mensagem': 'O usuário já existe'})
        if lista_qtd_funcio_nome > 0:
            return JsonResponse({'mensagem': 'O nome já existe'})

        funcionario.save()
        serializer = FuncionarioSerializer(funcionario, many=False)
        return JsonResponse({'objeto': serializer.data})

    if request.method == 'DELETE':
        existe_email = query_params.get('email')

        if existe_email:
            existe_funcionario = Funcionario.objects.filter(email=existe_email).first()

            if existe_funcionario:
                serializer = FuncionarioSerializer(existe_funcionario,many=False)
                existe_funcionario.delete()
                return JsonResponse({'objeto': serializer.data})

            return JsonResponse({'objeto': serializer.data})
        
        return JsonResponse({'mensagem': 'Usuario não encontrado'})
    
    if request.method == 'PUT':
        data = json.loads(request.body)
        email = query_params.get('email')

        email_existe = Funcionario.objects.filter(email=data.get('email')).count()
        if email_existe:
            return JsonResponse({'mensagem': 'Usuario já existe'})

        funcionario = Funcionario.objects.filter(email=email).first()
        if funcionario:
            funcionario.nome = data.get('nome')
            funcionario.sobrenome = data.get('sobrenome')
            funcionario.funcao = data.get('funcao')
            funcionario.email = data.get('email')
            funcionario.ano_nascimento = data.get('ano_nascimento')
            funcionario.save()
            serializer = FuncionarioSerializer(funcionario,many=False)
            return JsonResponse(serializer.data)

        return JsonResponse({'mensagem': 'Usuario não encontrado'})

    return JsonResponse({'mensagem': 'Método inválido'})

    # salvar so se for post quando mudar os nomes
    
  
# post adiciona funconario

