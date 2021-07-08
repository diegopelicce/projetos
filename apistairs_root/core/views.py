from django.shortcuts import render
from rest_framework import viewsets
from .models import HorarioDisponivel, TarefaAgendada
from .serializers import HorarioDisponivelSerializer, TarefaAgendadaSerializer


class HorarioDisponivelViewSet(viewsets.ModelViewSet):
    queryset = HorarioDisponivel.objects.all()
    serializer_class = HorarioDisponivelSerializer


class TarefaAgendadaViewSet(viewsets.ModelViewSet):
    queryset = TarefaAgendada.objects.all()
    serializer_class = TarefaAgendadaSerializer

