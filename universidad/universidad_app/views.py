from django.shortcuts import render, redirect
from .models import Facultad
from .models import Programa
from .models import Docente
from .forms import FacultadForm, ProgramaForm, DocenteForm


def facultades_list(request):
    facultades = Facultad.objects.all()
    return render(request, 'universidad_app/facultades_list.html', {'facultades': facultades})


def programas_list(request):
    programas = Programa.objects.all()
    return render(request, 'universidad_app/programas_list.html', {'programas': programas})


def docentes_list(request):
    docentes = Docente.objects.all()
    return render(request, 'universidad_app/docentes_list.html', {'docentes': docentes})

# -------Administrar Facultades-----------


def agregar_facultad(request):
    if request.method == 'POST':
        form = FacultadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('facultades_list')
    else:
        form = FacultadForm()
    return render(request, 'universidad_app/agregar_facultad.html', {'form': form})


def eliminar_facultad(request, facultad_id):
    facultad = Facultad.objects.get(id=facultad_id)
    facultad.delete()
    return redirect('facultades_list')

# -------Administrar Programas-----------


def agregar_programa(request):
    facultades = Facultad.objects.all()
    if request.method == 'POST':
        form = ProgramaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('programas_list')
    else:
        form = ProgramaForm()
    return render(request, 'universidad_app/agregar_programa.html', {'form': form, 'facultades': facultades})


def editar_programs(request, programa_id):
    programa = Programa.objects.get(id=programa_id)

    if request.method == 'POST':
        form = ProgramaForm(request.POST, instance=programa)
        if form.is_valid():
            form.save()
            return redirect('programas_list')
    else:
        form = ProgramaForm(instance=programa)

    return render(request, 'universidad_app/editar_programa.html', {'form': form})


def eliminar_programa(request, programa_id):
    programa = Programa.objects.get(id=programa_id)
    programa.delete()
    return redirect('programas_list')

# -------Administrar Docentes-----------


def agregar_docente(request):
    if request.method == 'POST':
        form = DocenteForm(request.POST)
        if form.is_valid():
            form.save()
            # Ajusta el nombre de la URL según tu configuración
            return redirect('docentes_list')
    else:
        form = DocenteForm()

    return render(request, 'universidad_app/agregar_docente.html', {'form': form})


def editar_docente(request, docente_id):
    docente = Docente.objects.get(id=docente_id)

    if request.method == 'POST':
        form = DocenteForm(request.POST, instance=docente)
        if form.is_valid():
            form.save()
            return redirect('docentes_list')
    else:
        form = DocenteForm(instance=docente)

    return render(request, 'universidad_app/editar_docente.html', {'form': form})


def eliminar_docente(request, docente_id):
    docente = Docente.objects.get(id=docente_id)
    docente.delete()
    return redirect('docentes_list')
