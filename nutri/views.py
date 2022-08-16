from ast import Delete
from gettext import NullTranslations
from django.shortcuts import redirect
from xmlrpc.client import DateTime
from django.shortcuts import render
from django.http import request
from .models import *
from .serializers import * 
from rest_framework import viewsets
from rest_framework import permissions
import datetime as dt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

dateformat = "%Y-%m-%dT%H:%M"

def HomeNutri(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    #meta = request.META
    #for key,value in meta.items():
    #    print(f'{key} -- {value}')
    return render(request, "homeNutri.html")

    
class ConsumoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Consumo.objects.all()
    serializer_class = ConsumoSerializer
    #permission_classes = [permissions.IsAuthenticated]


@login_required
def deletar(request,pk):
    context={}
    try:
        consumo = Consumo.objects.get(id=pk)
        context['obj'] = consumo
        context['now'] = consumo.data_refeicao.strftime(dateformat)
    except:
        context['message'] += 'REFEIÇÃO NÃO ENCONTRADA'
    if request.method == 'POST':
        consumo.delete()
    return redirect('listaRefeicao')


def lista(request):
    context={}
    context['users'] = User.objects.all()
    context['userdefault'] = User()
    context['date']=""

    if (request.GET.get('date')):
        context['date'] = request.GET.get('date')
    else:
        context['date'] = dt.date.today().strftime('%Y-%m-%d')
        date = dt.date.today().strftime('%d/%m/%Y')

    try:
        if request.GET.get('id_usuario'):
            context['userdefault'] = User.objects.get(pk = request.GET.get('id_usuario'))
    except:
        pass

    if context['userdefault'].id != None:
        if request.GET.get('date'):
            context['lista'] = Consumo.objects.filter(created_by = context['userdefault'] ,data_refeicao__date = request.GET.get('date')).order_by("-data_refeicao__date","data_refeicao__time")
        else:
            context['lista'] = Consumo.objects.filter(created_by = context['userdefault']).order_by("-data_refeicao__date","data_refeicao__time")
    else:
        if request.GET.get('date'):
            context['lista'] = Consumo.objects.filter(data_refeicao__date = request.GET.get('date')).order_by("-data_refeicao__date","data_refeicao__time")
        else:
            context['lista'] = Consumo.objects.all().order_by("-data_refeicao__date","data_refeicao__time")
    return render(request, 'lista.html',context)

@login_required
def inserir(request,pk=0):
    consumo = Consumo()
    context={}
    context['message'] = ""
    context['now'] = dt.datetime.now().strftime(dateformat)
    if pk != 0:
        try:
            consumo = Consumo.objects.get(id=pk)
            context['obj'] = consumo
            context['now'] = consumo.data_refeicao.strftime(dateformat)
        except:
            context['message'] += 'REFEIÇÃO NÃO ENCONTRADA'


    if request.method == 'POST':

        consumo.refeicao = request.POST.get('textrefeicao')
        dataref = dt.datetime.strptime(request.POST.get('datarefeicao'), dateformat)
        consumo.data_refeicao = dataref
        consumo.created_by = request.user

        if consumo.data_refeicao.hour >= 7 and consumo.data_refeicao.hour  < 12: 
            consumo.periodo=0
        if consumo.data_refeicao.hour >= 12 and consumo.data_refeicao.hour  < 18: 
            consumo.periodo=1
        if consumo.data_refeicao.hour >= 18 and consumo.data_refeicao.hour  <=23 : 
            consumo.periodo=2
        if consumo.data_refeicao.hour >= 0 and consumo.data_refeicao.hour  < 7: 
            consumo.periodo=3
        
        consumo.save()
        if consumo.id:
            context['message'] += "\nREFEIÇÃO ADICIONADA COM SUCESSO"
    return render(request, "inserir.html",context)
