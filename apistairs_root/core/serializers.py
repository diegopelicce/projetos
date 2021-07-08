from rest_framework import serializers
from .models import HorarioDisponivel, TarefaAgendada

# Serializers define the API representation.
class HorarioDisponivelSerializer(serializers.ModelSerializer):
    class Meta:
        model = HorarioDisponivel
        fields = ['id_horario', 'nome_barbeiro', 'data_horario', 'ativo']


class TarefaAgendadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TarefaAgendada
        fields = ['id_tarefa', 'id_horario_disponivel', 'nome_cliente']