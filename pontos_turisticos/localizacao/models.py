from django.db import models
# Create your models here.

class Localizacao(models.Model):
    endereco =  models.CharField(max_length=255, null=False,blank=True)
    cidade = models.CharField(max_length=255, null=False,blank=True)
    estado =  models.CharField(max_length=255, null=False,blank=True)
    pais =  models.CharField(max_length=255, null=False,blank=True)
    latitude = models.IntegerField(null = True)
    longitude = models.IntegerField(null = True)

    def __str__(self):
        return self.endereco
    class Meta:
        verbose_name =  "Localizacao"

