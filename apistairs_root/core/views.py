from django.shortcuts import render
from rest_framework import viewsets
from .models import HorarioDisponivel, TarefaAgendada, Usuario
from .serializers import HorarioDisponivelSerializer, TarefaAgendadaSerializer, UsuarioSerializer


class HorarioDisponivelViewSet(viewsets.ModelViewSet):
    queryset = HorarioDisponivel.objects.all()
    serializer_class = HorarioDisponivelSerializer

class TarefaAgendadaViewSet(viewsets.ModelViewSet):
    queryset = TarefaAgendada.objects.all()
    serializer_class = TarefaAgendadaSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

