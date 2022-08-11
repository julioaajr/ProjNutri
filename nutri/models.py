from django.db import models
from django.contrib.auth.models import User
class refeicoes (models.Model):
    STATUS = (
        ('0', 'Manhã'),
        ('1', 'Tarde'),
        ('2', 'Noite'),
        ('3', 'Madrugada'),

    )   
    refeicao = models.TextField()
    data_refeicao = models.DateTimeField(auto_now=True, verbose_name="Data da Refeição")
    created_at = models.DateTimeField(auto_now=True, verbose_name="Criado em.")
    created_by = models.ForeignKey(User, models.DO_NOTHING, blank = True, null = True, related_name="createdbyclient", verbose_name="Criado por")