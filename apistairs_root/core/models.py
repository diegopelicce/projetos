from django.db import models

# Create your models here.
class HorarioDisponivel(models.Model):
    id_horario = models.AutoField(primary_key=True)
    nome_barbeiro = models.CharField(max_length=255, default='')
    data_horario = models.DateTimeField(null=False)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.data_horario


class TarefaAgendada(models.Model):
    id_tarefa = models.AutoField(primary_key=True)
    id_horario_disponivel = models.CharField(max_length=5)
    nome_cliente = models.CharField(max_length=255)

    def __str__(self):
        return self.nome_cliente