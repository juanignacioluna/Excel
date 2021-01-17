from django.db import models

class hojas(models.Model):

	titulo = models.CharField(max_length=200)
	columnas = models.TextField()
	celdas = models.TextField()
