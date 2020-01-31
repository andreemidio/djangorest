from rest_framework import viewsets
from comentarios.models import Comentario
from .serializers import AtracoesSerializer



class ComentariosSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Comentario.objects.all()
    serializer_class = AtracoesSerializer