from typing import Any
from django.db import models
from django.db.models import Sum
# Create your models here.


class Presente(models.Model):
    nome = models.CharField(max_length=70)
    qtd = models.IntegerField()
    ativo = models.BooleanField(default = True)
    percent = models.FloatField()
    
    def atualiza_percent(self):
        num_cotas = self.cotas.all().aggregate(total = Sum('qtd'))['total']
        if num_cotas == None:
            num_cotas = 0
        if self.qtd <= 0 or self.qtd == None:
            self.qtd =50
            self.save()
        x = num_cotas/self.qtd*100
        if x > 100:
            x = 100
        return f"{x:.1f}"
    
    @property
    def porcentagem(self):
        return str(self.percent)


    
    def __str__(self):
        return (f"{self.nome} - qtd {self.qtd}")


class Cota(models.Model):
    presente = models.ForeignKey(Presente,null = False, blank = False,on_delete = models.DO_NOTHING, related_name='cotas')
    nome = models.CharField(max_length=50, verbose_name = "Nome e Sobrenome")
    qtd = models.IntegerField(null = False, blank = False)
    def __str__(self):
        return (f"{self.nome} -- {self.qtd}")
   
