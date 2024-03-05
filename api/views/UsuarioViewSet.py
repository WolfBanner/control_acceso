from rest_framework import viewsets, permissions
from api.serializers.UsuarioSerializer import UsuarioSerializer
from api.models import Usuario


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UsuarioSerializer
