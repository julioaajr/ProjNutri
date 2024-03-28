from django.shortcuts import render
from .models import * 

# Create your views here.

def Homecha(request):
    context = {}
    context['presentes'] = Presente.objects.filter(ativo=True)
    for i in context['presentes']:
        i.percent = i.porcentagem
        print (i.percent)

    print('---------')
    context['presentes'] = context['presentes'].filter(ativo = True ).order_by('percent')
    for i in context['presentes']:
        print (f"{i.percent} -- {i.nome}")

    return render(request, "dashboardbebe.html",context)
