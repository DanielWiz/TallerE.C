from django.db import models
from vote.models import VoteModel
from datetime import datetime

class Propuesta(models.Model):
    IdPropuesta = models.AutoField(primary_key=True)
    PropuestaNombre = models.CharField(max_length=500)
    PropuestaDetalle = models.TextField(max_length=1000)

    def __str__(self):
    	return "%s - %s" % (self.IdPropuesta,self.PropuestaNombre)

class PropuestaAprobada(VoteModel, models.Model):
	IdPropuestaAprobada = models.AutoField(primary_key=True)
	PropuestaAprobadaNombre = models.CharField(max_length=500)
	PropuestaAprobadaDetalle = models.CharField(max_length=1000)

	def __str__(self):
		return "%s - %s" % (self.IdPropuestaAprobada,self.PropuestaAprobadaNombre)
		

class Taller(models.Model):
	codigo_taller = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=60)
	descripcion = models.CharField(max_length=120)
	fecha = models.DateTimeField(default=datetime.now())
	lugar_taller = models.CharField(max_length=60)
	imagen = models.ImageField(default='img_talleres/ejemplo.jpg')

	def __str__(self):
		return "%s. %s" % (self.codigo_taller, self.nombre)