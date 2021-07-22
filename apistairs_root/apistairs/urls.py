from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from core.views import HorarioDisponivelViewSet, TarefaAgendadaViewSet, UsuarioViewSet


router = routers.DefaultRouter()
router.register(r'horariodisponivel', HorarioDisponivelViewSet)
router.register(r'tarefaagendada', TarefaAgendadaViewSet)
router.register(r'usuario', UsuarioViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
