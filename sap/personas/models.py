from django.db import models


# Create your models here.
# class Domicilio(models.Model):
#     calle = models.CharField(max_length=255)
#     no_domicilio = models.IntegerField()
#     ciudad = models.CharField(max_length=255)
#
#     def __str__(self):
#         return f"  {self.calle} - {self.no_domicilio} - {self.ciudad} "


class Persona(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.EmailField()
    numero = models.IntegerField()
    dia = models.DateField(auto_now_add =True)
    calle = models.CharField(max_length=255, blank=True)
    no_domicilio = models.IntegerField()
    ciudad = models.CharField(max_length=255)
    metodoPago = models.CharField(max_length=255,default=True,blank=True,null=True)
    total = models.IntegerField(default=True,blank=True,null=True)
    deuda = models.IntegerField(default=True,blank=True,null=True)


    # domicilio = models.ForeignKey(Domicilio, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Persona: {self.id} - {self.nombre} - {self.apellido} - {self.email} -{self.numero} - {self.dia} - {self.calle} {self.no_domicilio} - {self.ciudad} - {self.total} "
