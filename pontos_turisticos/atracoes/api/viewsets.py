
from rest_framework import viewsets
from atracoes.models import Atracoes
from .serializers import AtracoesSerializer



class AtracoesSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Atracoes.objects.all()
    serializer_class = AtracoesSerializer