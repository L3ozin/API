import email
from .models import Curriculo, Perfil, Pessoa, Funcionario
from rest_framework import serializers


class FuncionarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Funcionario
        fields = ['id','nome', 'sobrenome','funcao','email','ano_nascimento','created_at', 'updated_at']

class PerfilSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Perfil
        fields = ['id','nome', 'sobrenome','email''github','avatar','celular','perfil','created_at', 'updated_at']

class CurriculoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Curriculo
        fields = ['id','empresa', 'data_inicio','data_saida','empresa_atual','resumo','created_at', 'updated_at']