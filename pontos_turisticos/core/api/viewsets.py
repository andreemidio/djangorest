from rest_framework import viewsets
from core.models import PontoTuristico
from rest_framework.viewsets import ModelViewSet

from .serializers import PontoTuristicoSerializer



class PontoTuristicoSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    # queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer
    def get_queryset(self):

        return PontoTuristico.objects.filter(aprovado=True)