from django.db import models
from django.contrib.auth.models import User


class Consumo (models.Model):
    #['refeicao','periodo','data_refeicao','created_at','created_by']
    PERIODO = (
        ('0', 'Manhã'),
        ('1', 'Tarde'),
        ('2', 'Noite'),
        ('3', 'Madrugada'),

    )   
    refeicao = models.TextField()
    periodo = models.CharField(max_length=1, choices=PERIODO,default=0, verbose_name="Periodo")
    data_refeicao = models.DateTimeField(verbose_name="Data da Refeição")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em.")
    created_by = models.ForeignKey(User, models.DO_NOTHING, blank = True, null = True, related_name="createdbyclient", verbose_name="Criado por")
    
    def __str__(self):
        return (f"{self.data_refeicao} \n {self.refeicao} \n {self.created_by.first_name} \n ||| {self.created_at} |||")

    