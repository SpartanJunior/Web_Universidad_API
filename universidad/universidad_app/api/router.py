from rest_framework.routers import DefaultRouter
from .views import FacultadViewSet, ProgramaViewSet, DocenteViewSet

router_facultad = DefaultRouter()
router_programa = DefaultRouter()
router_docente = DefaultRouter()
router_facultad.register(prefix='crud', basename='crud', viewset = FacultadViewSet)
router_programa.register(prefix='crud', basename='crud', viewset = ProgramaViewSet)
router_docente.register(prefix='crud', basename='crud', viewset = DocenteViewSet)
