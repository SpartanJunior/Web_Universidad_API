from rest_framework.viewsets import ModelViewSet
from universidad_app.models import Facultad, Programa, Docente
from universidad_app.api.serializer import FacultadSerializer, ProgramaSerializer, DocenteSerializer

class FacultadViewSet(ModelViewSet):
	serializer_class = FacultadSerializer
	queryset = Facultad.objects.all()

class ProgramaViewSet(ModelViewSet):
	serializer_class = ProgramaSerializer
	queryset = Programa.objects.all()

class DocenteViewSet(ModelViewSet):
	serializer_class = DocenteSerializer
	queryset = Docente.objects.all()