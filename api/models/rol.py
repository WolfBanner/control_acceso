import uuid
from django.db import models

class Rol(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre