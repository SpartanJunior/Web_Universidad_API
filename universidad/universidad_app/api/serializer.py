from rest_framework.serializers import ModelSerializer
from universidad_app.models import Facultad, Programa, Docente

class FacultadSerializer(ModelSerializer):
    class Meta:
        model = Facultad
        fields = ['id', 'nombre']

class ProgramaSerializer(ModelSerializer):
    class Meta:
        model = Programa
        fields = ['id', 'nombre', 'facultad']

class DocenteSerializer(ModelSerializer):
    class Meta:
        model = Docente
        fields = ['id', 'nombre', 'programa']