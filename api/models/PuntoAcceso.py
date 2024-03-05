import uuid
from django.db import models
from .Horario import Horario
from .TipoAcceso import TipoAcceso


class PuntoAcceso(models.Model):
    id_punto = models.UUIDField(primary_key=True, default=uuid.uuid4)
    nombre = models.CharField(max_length=200)
    es_activo = models.BooleanField(default=True)
    tipo_acceso = models.ForeignKey(TipoAcceso, on_delete=models.CASCADE)
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
