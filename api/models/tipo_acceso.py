import uuid
from django.db import models

class TipoAcceso(models.Model):
    id_tipoacceso = models.UUIDField(primary_key=True, default=uuid.uuid4)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=200)
    es_activo = models.BooleanField(default=True)
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre