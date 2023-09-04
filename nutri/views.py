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
from django.db.models import Count
from .dashboard import *


datetimeformat = "%Y-%m-%dT%H:%M"
dateformat = "%Y-%m-%d"
PERIODO = (('0', 'Manhã'),('1', 'Tarde'),('2', 'Noite'),('3', 'Madrugada'))
PERIODO2 = ['Manhã','Tarde','Noite','Madrugada']


def HomeNutri(request):
    #x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
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
        context['now'] = consumo.data_refeicao.strftime(datetimeformat)
    except:
        context['message'] += 'REFEIÇÃO NÃO ENCONTRADA'
    if request.method == 'POST':
        consumo.delete()
    return redirect('listaRefeicao')


def lista(request):
    context={}
    context['periodo'] = PERIODO
    context['users'] = User.objects.all() #lista de usuarios para escolher
    context['userdefault'] = User() #usuario para manter o parametro selecionado
    context['date']=""
    context['lista']=""

    if (request.GET.get('date')):
        context['date'] = request.GET.get('date')

    if (request.GET.get('periodo')):
        context['periododefault'] = request.GET.get('periodo')

    try:
        if request.GET.get('id_usuario') and request.GET.get('id_usuario') != 'todos': #se não vier usuário ou se vier 'todos' não ira possuir um default
            context['userdefault'] = User.objects.get(pk = request.GET.get('id_usuario'))

        if(context['userdefault'].id == None and request.GET.get('id_usuario') == None): #não havendo default
            context['userdefault'] = User.objects.get(pk = request.user.id)

        if context['userdefault'].id != None: #Se não encontrar o USUARIO RETORNA as refeicoes de todos
            context['lista'] = Consumo.objects.filter(created_by = context['userdefault'])

        if(context['userdefault'].id == None or equest.GET.get('id_usuario') == 'todos'):
            context['lista'] = Consumo.objects.all()

        if request.GET.get('date'): # Se a lista não estiver vazia filtra pela data
            context['lista'] = context['lista'].filter(data_refeicao__date = request.GET.get('date'))
        
        if request.GET.get('periodo'):
            context['lista'] = context['lista'].filter(periodo = request.GET.get('periodo'))

        if context['lista'] != "": #Ordena a lista
            context['lista']= context['lista'].filter().order_by("-data_refeicao__date","created_by__first_name","data_refeicao__time")
    except:
        pass

    return render(request, 'lista.html',context)


@login_required
def inserir(request,pk=0):
    consumo = Consumo()
    context={}
    context['message'] = ""
    context['now'] = dt.datetime.now().strftime(datetimeformat)
    if pk != 0:
        try:
            consumo = Consumo.objects.get(id=pk)
            context['obj'] = consumo
            context['now'] = consumo.data_refeicao.strftime(datetimeformat)
        except:
            context['message'] += 'REFEIÇÃO NÃO ENCONTRADA'


    if request.method == 'POST':

        consumo.refeicao = request.POST.get('textrefeicao')
        dataref = dt.datetime.strptime(request.POST.get('datarefeicao'), datetimeformat)
        consumo.data_refeicao = dataref
        consumo.created_at = dataref - dt.timedelta(days=10)
        if pk == 0: # pk = 0 quer dizer que é uma inserção
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
        consumo.created_at = dataref - dt.timedelta(days=10)
        consumo.save()
        return redirect('listaRefeicao')

    return render(request, "inserir.html",context)


def dashboard(request):
    context = {}
    context['dashperiodo']=[]
    context['qtd_consumo'] = Consumo.objects.count()
    context['ultimo_consumo'] = Consumo.objects.last().data_refeicao
    context['periodo_frequente'] = Consumo.objects.values("periodo").annotate(count=Count('periodo')).order_by("-count")[0]
    context['periodo_frequente']['periodo'] = PERIODO[int(context['periodo_frequente']['periodo'])][1]
    context['progresso'] = '100'

    context['progresso_consumo'] = Consumo.objects.values("periodo").annotate(count=Count('periodo')).order_by("periodo")
    for i in context['progresso_consumo']:
        x = DashPeriodo()
        x.periodo = PERIODO2[int(i['periodo'])]
        x.contagem = int(i['count'])
        x.porcentagem = str(x.contagem/int(context['qtd_consumo'])*100)
        print(x.porcentagem)
        context['dashperiodo'].append(x)
    return render(request, "dashboard.html",context)
