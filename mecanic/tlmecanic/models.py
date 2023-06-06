from django.db import models

# Create your models here.
class vehiculo(models.Model):
    id_vehiculo         = models.AutoField(db_column='vehiculo', primary_key=True) 
    modelo_vehiculo     = models.CharField(max_length=20, blank=False, null=False)
    marca               = models.CharField(max_length=20)

    def __str__(self):
        return str(self.modelo_vehiculo)

class cliente(models.Model):
    rut              = models.CharField(primary_key=True, max_length=10)
    nombre           = models.CharField(max_length=20)
    apellido         = models.CharField(max_length=20)
    id_vehiculo      = models.ForeignKey('vehiculo',on_delete=models.CASCADE, db_column='vehiculo')  
    telefono         = models.CharField(max_length=45)
    email            = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    direccion        = models.CharField(max_length=50, blank=True, null=True)  
    

    def __str__(self):
        return str(self.nombre)+" "+str(self.apellido)   

class mecanico(models.Model):
    id_mecanico      = models.CharField(primary_key=True, max_length=10)
    nombre_mec       = models.CharField(max_length=20)
    apellido_mec     = models.CharField(max_length=20)
    id_vehiculo      = models.ForeignKey('vehiculo',on_delete=models.CASCADE, db_column='vehiculo')  
    tele             = models.CharField(max_length=45)
    email            = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    direccion        = models.CharField(max_length=50, blank=True, null=True)  
  

    def __str__(self):
        return str(self.nombre_mec)+" "+str(self.apellido_mec)   

class mantencion(models.Model):
    id_mecanico               = models.ForeignKey('mecanico',on_delete=models.CASCADE, db_column='mecanico')
    rut                       = models.ForeignKey('cliente',on_delete=models.CASCADE, db_column='cliente')
    id_vehiculo               = models.ForeignKey('vehiculo',on_delete=models.CASCADE, db_column='vehiculo')
    descripcion_mantencion    = models.CharField(max_length=300, blank=False, null=False)
    fecha_mantencion          = models.DateField(blank=False, null=False) 

    

    def __str__(self):
        return str(self.descripcion_mantencion)
    


class mantencion_repuesto(models.Model):
    id_rep                    = models.ForeignKey('repuesto',on_delete=models.CASCADE, db_column='repuesto')
    id_mecanico               = models.ForeignKey('mecanico',on_delete=models.CASCADE, db_column='mecanico')
    rut                       = models.ForeignKey('cliente',on_delete=models.CASCADE, db_column='cliente')
    id_vehiculo               = models.ForeignKey('vehiculo',on_delete=models.CASCADE, db_column='vehiculo')
    descripcion_mantencion    = models.CharField(max_length=300, blank=False, null=False)
    fecha_mantencion          = models.DateField(blank=False, null=False) 

    

    def __str__(self):
        return str(self.descripcion_mantencion)
    


    
class repuesto(models.Model):
    id_rep        = models.AutoField(db_column='respuesto', primary_key=True)
    tipo_repuesto       = models.CharField(max_length=20, blank=False, null=False)
    stock_rep           = models.CharField(max_length=20)

    def __str__(self):
        return str(self.tipo_repuesto)



