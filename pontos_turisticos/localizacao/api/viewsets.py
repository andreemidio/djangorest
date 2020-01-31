from rest_framework import viewsets
from localizacao.models import Localizacao
from .serializers import LocalizacaoSerializer



class LocalizacaoSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Localizacao.objects.all()
    serializer_class = LocalizacaoSerializer