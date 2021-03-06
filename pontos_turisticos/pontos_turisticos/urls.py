"""pontos_turisticos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import include, path
from rest_framework import routers
from core.api.viewsets import PontoTuristicoSet
from atracoes.api.viewsets import AtracoesSet
from comentarios.api.viewsets import ComentariosSet
from localizacao.api.viewsets import LocalizacaoSet
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'ponto-turistico', PontoTuristicoSet, basename='PontoTuristico')
router.register(r'comentarios', ComentariosSet, basename='Comentarios')
router.register(r'atracoes', AtracoesSet, basename='Atracoes')
router.register(r'localizacao', LocalizacaoSet, basename='Localizacao')



urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]




