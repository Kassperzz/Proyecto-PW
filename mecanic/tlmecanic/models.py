from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.

class usuarioBase(BaseUserManager):
    def create_user(self, email, nombre_completo, rut, password = None):
        if not email:
            raise ValueError("Error, debe tener correo!!")
        cliente = self.model(email = self.normalize_email(email), nombre_completo = nombre_completo, rut = rut)
        cliente.set_password(password)
        cliente.save()
        return cliente
    
    def create_superuser(self,email, nombre_completo, rut, password ):
        cliente = self.create_user(email, nombre_completo= nombre_completo, rut= rut, password=password)
        cliente.is_admin = True 
        cliente.save()
        return cliente


class vehiculo(models.Model):
    id_vehiculo         = models.AutoField(db_column='vehiculo', primary_key=True)
    rut                 = models.ForeignKey('cliente',on_delete=models.CASCADE, db_column='cliente') 
    modelo_vehiculo     = models.CharField(max_length=20, blank=False, null=False)
    marca               = models.CharField(max_length=20)

    def __str__(self):
        return str(self.modelo_vehiculo)

class cliente(AbstractBaseUser):
    rut              = models.CharField(primary_key=True, max_length=10)
    nombre_completo  = models.CharField(max_length=100)
    telefono         = models.CharField(max_length=45)
    email            = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    direccion        = models.CharField(max_length=50, blank=True, null=True)  
    estado          = models.BooleanField(default=True)
    is_admin        = models.BooleanField(default=False)
    objects = usuarioBase() 

    password = models.CharField(max_length=15, null=False, default="")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre_completo','rut']

    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self,app_label):
        return True
    
    @property
    def is_staff(self):
            return self.is_admin
    
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



