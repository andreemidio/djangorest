from rest_framework import viewsets, response
from core.models import PontoTuristico
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import PontoTuristicoSerializer

from rest_framework import viewsets
from rest_framework.response import Response

class PontoTuristicoSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer


    # def get_queryset(self):
    #     return PontoTuristico.objects.filter(aprovado=True)
    #
    # def list(self, request, *args, **kwargs):
    #     return Response()
    #
    # def create(self, request, *args, **kwargs):
    #     return Response(request.data)
    #
    # def retrieve(self, request, *args, **kwargs):
    #     return Response(request.data)
    #
    # def destroy(self, request, *args, **kwargs):
    #     return Response(request.data)