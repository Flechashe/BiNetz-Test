from django.db import models
# Create your models here.
# https://docs.djangoproject.com/en/4.0/topics/db/models/


class Patient(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.PositiveIntegerField()
    email = models.EmailField(max_length=100)
    fecha_de_nacimiento = models.DateField()
    SEXOS = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
    sexo = models.CharField(max_length=1, choices=SEXOS)
    cobertura_medica = models.CharField('cobertura médica', max_length=50)

    class Meta:
        db_table = 'patient'
