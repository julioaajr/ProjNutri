from django.shortcuts import render
from .models import * 

# Create your views here.

def Homecha(request):
    context = {}
    context['presentes'] = Presente.objects.all()

    return render(request, "dashboardbebe.html",context)
