import uuid
from django.db import models
from .PuntoAcceso import PuntoAcceso


class Reporte(models.Model):
    id_reporte = models.UUIDField(primary_key=True, default=uuid.uuid4)
    id_punto_acceso = models.ForeignKey(PuntoAcceso, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.created_at)
