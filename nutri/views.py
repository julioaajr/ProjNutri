from django.shortcuts import render
from django.http import request
from .models import *
from .serializers import * 
from rest_framework import viewsets
from rest_framework import permissions
import datetime

def Index(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    #meta = request.META
    #for key,value in meta.items():
    #    print(f'{key} -- {value}')
    return render(request, "index.html")

    
class ConsumoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Consumo.objects.all()
    serializer_class = ConsumoSerializer
    permission_classes = [permissions.IsAuthenticated]

def lista(request):
    context={}
    if request.GET.get('date'):
        context['lista'] = Consumo.objects.filter(data_refeicao__date = request.GET.get('date')).order_by("-data_refeicao__date","data_refeicao__time")
    else:
        context['lista'] = Consumo.objects.all().order_by("-data_refeicao__date","data_refeicao__time")
    return render(request, 'lista.html',context)


def inserir(request):
    context={}
    context['message'] = ""
    if request.method == 'POST':
        print(request.POST.get('textrefeicao'))
        print(request.POST.get('datarefeicao'))
        consumo = Consumo()
        consumo.refeicao = request.POST.get('textrefeicao')
        consumo.data_refeicao =request.POST.get('datarefeicao')
        consumo.save()
        if consumo.id:
            context['message'] += "\nREFEIÇÃO ADICIONADA COM SUCESSO"
    

    return render(request, "inserir.html",context)
