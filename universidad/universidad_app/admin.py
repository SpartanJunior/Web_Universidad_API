from django.contrib import admin
from .models import Facultad, Programa, Docente

# admin.site.register(Facultad)
admin.site.register(Programa)
admin.site.register(Docente)

@admin.register(Facultad)

class FacultadAdmin(admin.ModelAdmin):
    list_display=['id', 'nombre']