from django.db import models
from atracoes.models import Atracoes
#from comentarios.models import Comentario
from localizacao.models import Localizacao



# Create your models here.
class PontoTuristico(models.Model):
    nome = models.CharField(max_length=250, null = False, blank=True)
    descricao = models.TextField(null = False, blank=True)
    aprovado = models.BooleanField(null = False, default=False)
    atracoes =  models.ManyToManyField(Atracoes)
    #comentario =  models.ManyToManyField(Comentario)
    localizacao  = models.ForeignKey(Localizacao, on_delete=models.CASCADE)
    visivel = models.BooleanField()

    def __str__(self):
        return self.nome
    class Meta:
        verbose_name =  "PontoTuristico"