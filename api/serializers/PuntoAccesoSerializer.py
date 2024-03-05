from rest_framework import serializers

from api.models import PuntoAcceso


class PuntoAccesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PuntoAcceso
        fields = '__all__'
