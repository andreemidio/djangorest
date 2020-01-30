from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Comentario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField(null=True, blank=True)
    nota = models.DecimalField(max_digits = 10, decimal_places=0)
    data = models.DateTimeField(auto_now_add=True)
    visivel = models.BooleanField()
    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name =  "Comentario"