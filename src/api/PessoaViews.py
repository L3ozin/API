'''Modulo que salva a classe PessoaViews'''

from django.http import JsonResponse

def hello_pessoa(request, name):
    return JsonResponse('ola pessoa', safe=False)
