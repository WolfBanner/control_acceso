from rest_framework import viewsets, permissions

from api.models import Horario
from api.serializers.HorarioSerializer import HorarioSerializer

class HorarioViewSet(viewsets.ModelViewSet):
    queryset = Horario.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = HorarioSerializer