from rest_framework import serializers
from .models import HorarioDisponivel, TarefaAgendada, Usuario

# Serializers define the API representation.
class HorarioDisponivelSerializer(serializers.ModelSerializer):
    class Meta:
        model = HorarioDisponivel
        fields = ['id_horario', 'id_barbeiro', 'data', 'horario', 'ativo']


class TarefaAgendadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TarefaAgendada
        fields = ['id_tarefa', 'id_horario_disponivel', 'nome_cliente']

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id_user', 'nome_user']