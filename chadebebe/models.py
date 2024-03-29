from django.db import models

# Create your models here.


class Presente(models.Model):
    nome = models.CharField(max_length=70)
    qtd = models.IntegerField()
    ativo = models.BooleanField(default = True)
    percent = models.FloatField()
    
    @property
    def num_cotas(self):
        aux = self.cotas.all()
        soma = 0
        for i in aux:
            soma += i.qtd
        return soma
    
    @property
    def porcentagem(self):
        porcentagem = self.num_cotas / self.qtd * 100
        if porcentagem >= 100:
            return '100'
        else:
            return (f"{porcentagem:.1f}")

    
    
    def __str__(self):
        return (f"{self.nome} qtd {self.qtd}")


class Cota(models.Model):
    presente = models.ForeignKey(Presente,null = False, blank = False,on_delete = models.DO_NOTHING, related_name='cotas')
    nome = models.CharField(max_length=50, verbose_name = "Nome e Sobrenome")
    qtd = models.IntegerField(null = False, blank = False)
    def __str__(self):
        return (f"{self.nome}")