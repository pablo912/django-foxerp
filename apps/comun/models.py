from django.db import models
from apps.users.models import User
from apps.base.models import BaseModel
from django_tenants.models import TenantMixin, DomainMixin
 





class Company(BaseModel):

    ruc = models.CharField('ruc', max_length=11, unique = True, null = False, blank = False )
    name = models.CharField('nombre', max_length=250, null = False, blank = False )
    direction = models.CharField('direccion', max_length=250 )
    email = models.EmailField('correo', max_length=250, null = True, blank = True )
    user = models.ForeignKey( User, models.CASCADE, verbose_name = "Usuario", null = True )
    
    class Meta:

        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):

        return self.name

class CompanySchema(TenantMixin,BaseModel):

    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    auto_create_schema = True

    auto_drop_schema = True

class Domain(DomainMixin):
    pass



class Department(BaseModel):

    id = models.CharField( max_length=20, primary_key=True )
    description = models.CharField( max_length=200 )
    
    class Meta:
    
       verbose_name_plural = "Departamentos"
       verbose_name = "Departamento"
     
    def __str__(self):

        return self.id

class Province(BaseModel):

    id = models.CharField( max_length=20, primary_key=True )
    description = models.CharField( max_length=200 )    
    department = models.ForeignKey( Department, on_delete=models.CASCADE )

    class Meta:
        
       verbose_name_plural = "Provincias"
       verbose_name = "Provincia"

    def __str__(self):

        return self.description
    
class District(BaseModel):

    id = models.CharField( max_length=20, primary_key=True )

    description = models.CharField( max_length=200 )    
    province = models.ForeignKey( Province, on_delete=models.CASCADE )

    class Meta:
        
        verbose_name_plural = "Distritos"
        verbose_name = "Distrito"

    def __str__(self):

        return self.description

class Address(BaseModel):

        id = models.CharField( max_length=200, primary_key=True )
        description = models.CharField( max_length=255 )  

        class Meta:
        
            verbose_name_plural = "Tipos de direcciones"
            verbose_name = "Direccion"

           
        def __str__(self):

            return self.description

class IdentityDocument(BaseModel):


    id = models.CharField( max_length=200, primary_key=True )
    description = models.CharField( max_length = 200 )

    class Meta:
        
        verbose_name_plural = "docuumentos de identidades"
        verbose_name = "docuumento de identidad"

    def __str__(self):
        
        return self.description
    
class PersonType(BaseModel):
  
        description = models.TextField()

        class Meta:
            
            verbose_name_plural = "Tipos de personas"
            verbose_name = "Tipo de perosna"

        def __str__(self):

            return self.description

class Module(BaseModel):


    name = models.CharField('nombre', max_length=250, null = False, blank = False )

    class Meta:

        verbose_name = 'Modulo'
        verbose_name_plural = 'Modulos'

    def __str__(self):

        return self.name
    
class ItemType(models.Model):

    id = models.CharField( max_length=2, primary_key=True )
    description  = models.CharField(max_length=255)  


    class Meta:

        verbose_name_plural = 'tipo de producto'
        verbose_name = 'tipos de producto'
       
    def __str__(self):

        return self.description

class AffectationIgv( models.Model ):

        id = models.CharField( max_length=200, primary_key=True )
        state = models.BooleanField(default=True)
        exportation = models.BooleanField(default=False)
        free = models.BooleanField(default=False)
        description = models.CharField( max_length=200 )

        class Meta:


            verbose_name_plural = 'tipo de afectación igv'
            verbose_name = 'tipos de afectación igv'

        def __str__(self):

            return self.description

class Unit(models.Model):

        id = models.CharField( max_length=20, primary_key=True )
        state = models.BooleanField( default=True )
        symbol = models.CharField( max_length=200, null=True, blank=True )
        description = models.CharField( max_length=200 )
	 
        class Meta:
        
      
            verbose_name_plural = "Tipo de unidad"
            verbose_name = "tipos de unidades"

        def __str__(self):

            return self.description

class Currency(models.Model):
    
    id = models.CharField( max_length=200, primary_key=True )
    state = models.BooleanField( default = True )
    symbol = models.CharField(max_length=200)
    description = models.CharField( max_length=200 )

    class Meta:
        
        verbose_name_plural = "Currencies"
        verbose_name = "Currency"

    def __str__(self):

        return self.description


class DocumentType(models.Model):

        id = models.CharField( max_length=200, primary_key=True )
        state  = models.BooleanField( default=True )
        short = models.CharField( max_length=200, null=True, blank=True )
        description = models.CharField( max_length=200 )

        class Meta:
            
            verbose_name_plural = "Tipo de documento"
            verbose_name = "Tipos de documentos"

        def __str__(self):
            
            return self.description

class PaymentMethodType(models.Model):

        id = models.CharField( max_length=200, primary_key=True )
        state = models.BooleanField( default=True )
        description = models.CharField( max_length=200 )

        class Meta:
        
            verbose_name_plural = "Tipo de metodo de pago"
            verbose_name = "Tipos de metodos de pagos"

        def __str__(self):
            
            return self.description
        
class OperationType(models.Model):


        id = models.CharField( max_length=200, primary_key=True )
        state = models.BooleanField(default=True)
        exportation = models.BooleanField(default=True)
        description = models.CharField( max_length=200 )
          

        class Meta:

            verbose_name = "Tipo de operacion"
            verbose_name_plural = "Tipos de operaciones"


        def __str__(self):

            return self.description

class PaymentCondition(models.Model):

        id = models.CharField( max_length=200, primary_key=True )
        name = models.CharField( max_length=200 )
        days = models.IntegerField( default=0 )
        locked = models.BooleanField( default=False )
        state = models.BooleanField( default=True )

        class Meta:
            
            verbose_name = "Condicion de pago"
            verbose_name_plural = "Condiciones de pago"

        def __str__(self):

            return self.name



