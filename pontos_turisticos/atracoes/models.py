from django.db import models

# Create your models here.


class Atracoes(models.Model):
    nome_atracao = models.CharField(max_length=150)
    descricao =  models.TextField()
    horario_de_funcionamento = models.TextField()
    idade_minima = models.IntegerField()
    localizacao =  models.TextField()



    def __str__(self):
        return self.nome_atracao

    class Meta:
        verbose_name = "Atracoe"