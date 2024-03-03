import uuid
from django.contrib.auth.models import User
from django.db import models
from api.models import Rol


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_usuario = models.UUIDField(primary_key=True, default=uuid.uuid4)
    nombre = models.CharField(max_length=200)
    solapin = models.CharField(max_length=200)
    es_activo = models.BooleanField(default=True)
    rol = models.ManyToManyField(Rol, related_name='usuarios')

    def __str__(self):
        return self.nombre
