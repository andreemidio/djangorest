
from rest_framework import viewsets, request
from atracoes.models import Atracoes
from .serializers import AtracoesSerializer


from rest_framework import viewsets
from rest_framework.response import Response

class AtracoesSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Atracoes.objects.all()
    serializer_class = AtracoesSerializer


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