from django.db import models

class Facultad(models.Model):
    nombre = models.CharField(max_length=100)

class Programa(models.Model):
    nombre = models.CharField(max_length=100)
    facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE)

class Docente(models.Model):
    nombre = models.CharField(max_length=100)
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE)

