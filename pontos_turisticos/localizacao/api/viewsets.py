from rest_framework import viewsets, request
from localizacao.models import Localizacao
from .serializers import LocalizacaoSerializer
from rest_framework import viewsets
from rest_framework.response import Response


class LocalizacaoSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Localizacao.objects.all()
    serializer_class = LocalizacaoSerializer
    #
    #
    # def get_queryset(self):
    #     return Response(request.data)
    #
    # def list(self, request, *args, **kwargs):
    #     return Response(request.data)
    #
    # def create(self, request, *args, **kwargs):
    #     return Response(request.data)
    #
    # def retrieve(self, request, *args, **kwargs):
    #     return Response(request.data)
    #
    # def destroy(self, request, *args, **kwargs):
    #     return Response(request.data)