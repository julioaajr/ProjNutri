from .models import *
from rest_framework import serializers


class RefeicoesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = refeicoes
        fields = ['id','url','refeicao','periodo','data_refeicao','created_at','created_by']

