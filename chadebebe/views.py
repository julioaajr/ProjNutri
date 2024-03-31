from django.shortcuts import render, redirect
from .models import * 

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

    return redirect('homecha')      
