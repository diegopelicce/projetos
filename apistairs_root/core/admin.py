from django.contrib import admin
from .models import HorarioDisponivel, TarefaAgendada, Usuario

admin.site.register(HorarioDisponivel)
admin.site.register(TarefaAgendada)
admin.site.register(Usuario)
