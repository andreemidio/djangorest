from django.db import models



# Create your models here.
class PontoTuristico(models.Model):
    nome = models.CharField(max_length=250, null = False, blank=True)
    descricao = models.TextField(null = False, blank=True)
    aprovado = models.BooleanField(null = False, default=False)
    #atracoes =  models.ManyToManyField(Atracoes)

    def __str__(self):
        return self.nome, \
               self.descricao, \
               self.aprovado