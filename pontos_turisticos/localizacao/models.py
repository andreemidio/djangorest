from django.db import models
from core.models import PontoTuristico
# Create your models here.
class Localizacao(models.Model):
    endereco =  models.CharField(max_length=255, null=False,blank=True)
    ponto_turistico = models.ManyToManyField(PontoTuristico)

    def __str__(self):
        return self.endereco, \
               self.ponto_turistico
    class Meta:
        verbose_name =  "Localizacao"