from django.db import models

class HorarioDisponivel(models.Model):
    id_horario = models.AutoField(primary_key=True)
    id_barbeiro = models.CharField(max_length=255, default='', null=False, blank=False)
    data = models.DateField(default='', null=False)
    horario = models.TimeField(max_length=50, default='', null=False)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.data_horario


class TarefaAgendada(models.Model):
    id_tarefa = models.AutoField(primary_key=True)
    id_horario_disponivel = models.CharField(max_length=5, null=False)
    nome_cliente = models.CharField(max_length=255, null=False)
    email_cliente = models.CharField(max_length=255, default='', null=False)
    cpf_cliente = models.CharField(max_length=11, default='', null=False)

    def __str__(self):
        return self.nome_cliente


class Usuario(models.Model):
    id_user = models.AutoField(primary_key=True)
    nome_user = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.nome_user

