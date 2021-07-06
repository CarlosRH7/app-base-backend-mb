from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre =  models.CharField(max_length=50, null=True)
    edad =  models.PositiveSmallIntegerField(default=0)
    isMayorEdad = models.BooleanField(default=False)
    class Meta:
        db_table = 'usuarios'
