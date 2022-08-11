from .models import *
from rest_framework import serializers


class ConsumoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Consumo
        fields = ['id','url','refeicao','periodo','data_refeicao','created_at','created_by']


