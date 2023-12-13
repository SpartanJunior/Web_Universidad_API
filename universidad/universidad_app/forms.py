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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['facultad'].queryset = self.fields['facultad'].queryset.only(
            'nombre')
        self.fields['facultad'].widget.choices = [
            (facultad.id, facultad.nombre) for facultad in self.fields['facultad'].queryset]


class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = ['nombre', 'programa']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['programa'].queryset = self.fields['programa'].queryset.only(
            'nombre')
        self.fields['programa'].widget.choices = [
            (programa.id, programa.nombre) for programa in self.fields['programa'].queryset]
