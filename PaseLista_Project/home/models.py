from django.db import models

# Create your models here.

#Modelo de alumno
class Alumno(models.Model):
    nombre_alumno=models.CharField(max_length=30)

    def __str__(self):
        return self.nombre_alumno

#Modelo de asistencias
class Asistencia(models.Model):
    id_clases=models.ForeignKey('Clase',on_delete=models.CASCADE)
    id_alumno=models.ForeignKey(Alumno,on_delete=models.CASCADE)
    fecha_hora=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fecha_hora

#Modelo de clases
class Clase(models.Model):
    fecha=models.DateField()
    hora_inicio=models.TimeField()
    hora_fin=models.TimeField()
    id_asistencias=models.ForeignKey(Asistencia,on_delete=models.CASCADE)
    extras=models.CharField(max_length=250)

    def __str__(self):
        return self.fecha

#Modelo de materias
class Materia(models.Model):
    nombre_materia=models.CharField(max_length=30)
    periodo=models.CharField(max_length=15)
    year=models.IntegerField(default=2020)
    id_clases=models.ForeignKey(Clase,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_materia

#Modelo de profesor
class Profesor(models.Model):
    nombre_profesor=models.CharField(max_length=30)
    id_materia=models.ForeignKey(Materia,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_profesor