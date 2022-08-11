from django.shortcuts import render
from django.http import request
from .models import *
from .serializers import * 
from rest_framework import viewsets
from rest_framework import permissions

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


