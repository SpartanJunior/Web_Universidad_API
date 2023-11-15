"""
URL configuration for universidad project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from universidad_app import views


urlpatterns = [
    path('facultades/', views.facultades_list, name='facultades_list'),
    path('programas/', views.programas_list, name='programas_list'),
    path('docentes/', views.docentes_list, name='docentes_list'),
    path('facultades/agregar/', views.agregar_facultad, name='agregar_facultad'),
    path('facultades/eliminar/<int:facultad_id>/', views.eliminar_facultad, name='eliminar_facultad'),
    path('programas/agregar/', views.agregar_programa, name='agregar_programa'),
    path('programas/eliminar/<int:programa_id>/', views.eliminar_programa, name='eliminar_programa'),
    path('docentes/agregar/', views.agregar_docente, name='agregar_docente'),
    path('docentes/eliminar/<int:docente_id>/', views.eliminar_docente, name='eliminar_docente'),
    path('editar_facultad/<int:facultad_id>/', views.editar_facultad, name='editar_facultad'),
    path('editar_programa/<int:programa_id>/', views.editar_programa, name='editar_programa'),
    path('editar_docente/<int:docente_id>/', views.editar_docente, name='editar_docente'),

    
    path('admin/', admin.site.urls),
]
