
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'consumo', ConsumoViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('lista/', lista, name ='listaRefeicao'),
    path('inserir/', inserir, name ='inserirRefeicao'),
    path('inserir/<int:pk>/', inserir, name ='editarRefeicao'),
    path('deletar/<int:pk>/', deletar, name ='deletarRefeicao'),
    
]
