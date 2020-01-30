from django.db import models
# Create your models here.


class Atracao(models.Model):
    nome = models.CharField(max_length=150)
    descricao =  models.TextField()
    horario_de_funcionamento = models.TextField()
    idade_minima = models.IntegerField()
    locallizacao =  models.TextField()
    #atracoes =  models.ForeignKey(Atracoes, on_delete=models.CASCADE())


    def __str__(self):
        return self.nome,\
               self.descricao, \
               self.horario_de_funcionamento, \
               self.idade_minima, \
               self.locallizacao