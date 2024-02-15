from django.db import models

# Create your models here.


class registro_jug(models.Model):
    dni = models.IntegerField()
    num_socio = models.IntegerField()
    contraseña = models.CharField(max_length=100)
