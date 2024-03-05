from rest_framework import routers
from api.views import HorarioViewSet, UsuarioViewSet

router = routers.DefaultRouter()

router.register('api/horario', HorarioViewSet, basename='horario')
router.register('api/usuario', UsuarioViewSet, basename='usuario')

urlpatterns = router.urls