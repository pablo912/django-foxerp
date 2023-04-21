from django.db import models
from apps.base.models import BaseModel
from apps.users.models import User
from apps.comun.models import *
# Create your models here.


class Establishment(BaseModel):


        description = models.CharField( max_length=200 )
        department = models.ForeignKey( Department, on_delete=models.CASCADE )
        province = models.ForeignKey( Province, on_delete=models.CASCADE )
        district = models.ForeignKey( District, on_delete=models.CASCADE  )
        address = models.TextField()
        email = models.CharField( max_length=200 )
        phone = models.CharField( max_length=200, null=True, blank=True )
        code = models.CharField( max_length=200 )
        aditional_information  = models.CharField( max_length=200, null=True, blank=True )
        web_address =  models.CharField( max_length=200, null=True, blank=True )
        trade_address = models.CharField( max_length=200, null=True, blank=True )
        customer_id = models.IntegerField( default=0, null=True, blank=True)
        logo = models.ImageField(  null=True, blank=True )
        template_pdf =  models.CharField( max_length=200, null=True, blank=True )
        has_igv  = models.BooleanField( default=False )
        template_ticket_pdf = models.CharField( max_length=200, null=True, blank=True )


        class Meta:

            verbose_name_plural = 'establecimientos'
            verbose_name = 'establecimiento'
            
        def __str__(self):

            return self.description


class Warehouse(BaseModel):

        establishment = models.ForeignKey( Establishment, on_delete=models.CASCADE )
        description = models.CharField(max_length=200)


        class Meta:

            verbose_name = 'Deposito'
            verbose_name_plural = 'Depositos'

        def __str__(self):

            return self.description


class Serie(BaseModel):

        establishment = models.ForeignKey( Establishment, on_delete=models.CASCADE  )
        document_type = models.ForeignKey( DocumentType, on_delete=models.CASCADE )
        number = models.CharField( max_length=50)
        contingency = models.BooleanField( default=False )


        class Meta:

            verbose_name = "Serie"
            verbose_name_plural = "Series"

        def __str__(self):
              
              return self.number



class Client(BaseModel):

            type = models.CharField( max_length=20, choices=[ ('customers', 'customers'),
            ('suppliers', 'suppliers'),], null=True, blank=True )

            identity_document_type = models.ForeignKey( IdentityDocument, on_delete=models.CASCADE, null=True, blank=True )
            number = models.CharField( max_length = 200, null=True, blank=True )
            name = models.CharField( max_length=200 )
            trade_name = models.CharField( max_length = 200, null=True, blank=True )
            department = models.ForeignKey( Department, on_delete=models.CASCADE, null=True, blank=True )
            province = models.ForeignKey( Province, on_delete=models.CASCADE, null=True, blank=True )
            district = models.ForeignKey( District, on_delete=models.CASCADE, null=True, blank=True )
            address_type = models.ForeignKey( Address, on_delete=models.CASCADE, null=True, blank=True )
            address = models.CharField( max_length = 200, null=True, blank=True  )
            condition = models.CharField( max_length = 200, null=True , blank=True)
            email = models.CharField( max_length = 200, null=True , blank=True)
            phone = models.CharField( max_length = 200, null=True , blank=True)
            person_type = models.ForeignKey( PersonType, on_delete=models.CASCADE, null=True, blank=True )
            credit_days = models.SmallIntegerField( default = 0, null=True, blank=True )
            user = models.ForeignKey( User, on_delete=models.CASCADE, null=True, blank=True )
            company = models.ForeignKey( Company, on_delete = models.CASCADE, null=True, blank=True  )
            


            class Meta:

                verbose_name_plural = "clientes"
                verbose_name = "cliente"
                ordering = ['-id']

            def __str__(self):

                return self.name
            



class Item(BaseModel):

        has_igv = models.BooleanField( default = True  )
        calculate_quantity = models.BooleanField( default = True  )
        has_plastic_tax = models.BooleanField( default = False  )
        name = models.CharField(max_length=255, unique = True)
        description = models.TextField(null=True, blank=True)
        affectation_igv = models.ForeignKey( AffectationIgv, on_delete=models.CASCADE )
        model = models.CharField(max_length=100, null=True, blank=True)
        unit = models.ForeignKey( Unit, on_delete=models.CASCADE )
        currency = models.ForeignKey( Currency, on_delete =models.CASCADE  )
        price = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
        stock  =  models.DecimalField(max_digits=12, decimal_places=2, default= 0.00)
        stock_min  =  models.DecimalField(max_digits=12, decimal_places=2, default= 0.00)
        date_of_due = models.DateField( null=True, blank=True  )
        itemcode = models.CharField(max_length=200, null=True, blank=True )
        sunatcode = models.CharField(max_length=100, null=True, blank=True)
        barcode = models.CharField(max_length=100, null=True, blank=True)
        item_type = models.ForeignKey(ItemType, on_delete=models.CASCADE )
        amount_plastic_bag_taxes = models.DecimalField(max_digits=9, decimal_places=2, default= 0.10)
        image = models.CharField( max_length=200, null=True, blank=True )
        image_medium = models.CharField( max_length=200, null=True, blank=True )
        image_small = models.CharField( max_length=200, null=True, blank=True )
        warehouse = models.ForeignKey( Warehouse, on_delete=models.CASCADE, null=True, blank=True )


        class Meta:

            verbose_name = 'producto'
            verbose_name_plural = 'productos'

        def __str__(self):

            return self.name



