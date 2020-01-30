from django.db import models
from atracoes.models import Atracoes
from comentarios.models import Comentario



# Create your models here.
class PontoTuristico(models.Model):
    nome = models.CharField(max_length=250, null = False, blank=True)
    descricao = models.TextField(null = False, blank=True)
    aprovado = models.BooleanField(null = False, default=False)
    atracoes =  models.ManyToManyField(Atracoes)
    comentario =  models.ManyToManyField(Comentario)
    visivel = models.BooleanField()

    def __str__(self):
        return self.nome, \
               self.descricao, \
               self.aprovado
    class Meta:
        verbose_name =  "PontoTuristico"