from rest_framework import viewsets, permissions
from api.serializers import PuntoAccesoSerializer
from api.models import PuntoAcceso


class PuntoAccesoViewSet(viewsets.ModelViewSet):
    queryset = PuntoAcceso.objects.all()
    serializer_class = PuntoAccesoSerializer
    permission_classes = [permissions.IsAuthenticated]
