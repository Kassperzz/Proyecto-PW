from django.db import models

# Create your models here.
class vehiculo(models.Model):
    id_vehiculo         = models.AutoField(db_column='vehiculo', primary_key=True) 
    modelo_vehiculo     = models.CharField(max_length=20, blank=False, null=False)
    marca               = models.CharField(max_length=20)

    def __str__(self):
        return str(self.genero)

class cliente(models.Model):
    rut              = models.CharField(primary_key=True, max_length=10)
    nombre           = models.CharField(max_length=20)
    apellido         = models.CharField(max_length=20)
    algo             = models.DateField(blank=False, null=False) 
    id_vehiculo      = models.ForeignKey('vehiculo',on_delete=models.CASCADE, db_column='vehiculo')  
    telefono         = models.CharField(max_length=45)
    email            = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    direccion        = models.CharField(max_length=50, blank=True, null=True)  
    activo           = models.IntegerField()

    def __str__(self):
        return str(self.nombre)+" "+str(self.apellido_paterno)   

class mecanico(models.Model):
    id_mecanico              = models.CharField(primary_key=True, max_length=10)
    nombre           = models.CharField(max_length=20)
    apellido         = models.CharField(max_length=20)
    algo             = models.DateField(blank=False, null=False) 
    id_vehiculo      = models.ForeignKey('vehiculo',on_delete=models.CASCADE, db_column='vehiculo')  
    telefono         = models.CharField(max_length=45)
    email            = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    direccion        = models.CharField(max_length=50, blank=True, null=True)  
    activo           = models.IntegerField()

    def __str__(self):
        return str(self.nombre)+" "+str(self.apellido_paterno)   

class estado_solicitud(models.Model):
    id_vehiculo         = models.AutoField(db_column='vehiculo', primary_key=True) 
    modelo_vehiculo     = models.CharField(max_length=20, blank=False, null=False)
    marca               = models.CharField(max_length=20)

    def __str__(self):
        return str(self.genero)

