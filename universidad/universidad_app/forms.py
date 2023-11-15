from django import forms
from .models import Facultad
from .models import Programa
from .models import Docente

class FacultadForm(forms.ModelForm):
    class Meta:
        model = Facultad
        fields = ['nombre']

class ProgramaForm(forms.ModelForm):
    class Meta:
        model = Programa
        fields = ['nombre', 'facultad']

class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = ['nombre', 'programa']
        
        