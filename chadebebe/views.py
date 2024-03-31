from django.shortcuts import render, redirect
from .models import * 
from django.contrib.messages import constants
from django.contrib import messages

# Create your views here.

def Homecha(request):
    context = {}
    context['presentes'] = Presente.objects.filter(ativo=True)
    for i in context['presentes']:
        i.percent = i.atualiza_percent()
        i.save()
    context['presentes'] = context['presentes'].order_by('percent')
    return render(request, "dashboardbebe.html",context)


def InsereCota(request,pk):
    if request.method == 'GET':
        context = {}
        context['presente'] = Presente.objects.get(pk = pk)
        return render(request, "insere.html",context)

    if request.method == 'POST':
        cota = Cota()
        presente = Presente.objects.get(pk =  request.POST.get('pres'))
        cota.presente = presente
        cota.nome = request.POST.get('nome')
        cota.qtd = request.POST.get('qtd')
        cota.save()
        messages.add_message(request, constants.SUCCESS, 'Seu presente foi salvo com sucesso.')

    return redirect('homecha')      

def Relatorio(request):
    context = {}
    context['cotas'] = Cota.objects.all()
    return render(request,'relatorio.html',context)
