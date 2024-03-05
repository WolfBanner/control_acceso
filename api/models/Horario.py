import uuid
from django.db import models

days = [
    (1, "Domingo"),
    (2, "Lunes"),
    (3, "Martes"),
    (4, "Miercoles"),
    (5, "Jueves"),
    (6, "Viernes"),
    (7, "Sabado")
]


class Horario(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    nombre = models.CharField(max_length=200)
    hora_inicio = models.DateTimeField()
    hora_fin = models.DateTimeField()
    dias_semana = models.IntegerField(choices=days)
    es_activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
