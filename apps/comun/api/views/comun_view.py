from rest_framework.response import Response
from rest_framework import generics, status, viewsets
from apps.comun.models import Company
from rest_framework.generics import CreateAPIView
from apps.base.api import GeneraListApiView
from apps.comun.api.serializers.comun_serializer import *
from rest_framework.authentication import TokenAuthentication
from apps.users.authentication_mixins import Authentication
from django.conf import settings
import psycopg2
from django.db import connection
from rest_framework.decorators import api_view
from apps.comun.models import Province, Department, District


    

class CompanyListApiView(generics.ListAPIView):

    serializer_class = CompanySerializer
    authentication_classes =  [ Authentication ] 

    def get_queryset(self):
        
        user = self.request.user

        if user.is_admin:
                
            model = self.get_serializer().Meta.model
            return model.objects.filter( state = True, user = user  )        

        

        model = self.get_serializer().Meta.model
        return model.objects.filter( state = True, user = user.created_by  )

class CompanyCrateApiView(generics.CreateAPIView):

    serializer_class = CompanySerializer
    authentication_classes = [ Authentication ]

    def post(self,request):

        serializer = self.serializer_class( data = request.data )

        if serializer.is_valid():

            user = self.request.user

            serializer.save(user = user)

            return Response({'message':'Empresa creada exitosamente'}, status = status.HTTP_201_CREATED )

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST )
    
class CompanyUpdateApiView(generics.UpdateAPIView):

    serializer_class = CompanySerializer
    authentication_classes = [ Authentication ]

    def get_queryset(self,pk):
       
       user = self.request.user

       if user:
        
         return self.get_serializer().Meta.model.objects.filter( id = pk ).filter( user = user  ).first()
      
       return Response({'error':'No existe un producto con estso datos'}, status = status.HTTP_400_BAD_REQUEST )
      
    def patch(self,request,pk=None):

        if self.get_queryset(pk):

            product_serializer = self.serializer_class( self.get_queryset( pk ) )
            return Response( product_serializer.data, status = status.HTTP_200_OK )
        
        return Response({'error':'No existe un producto con estso datos'}, status = status.HTTP_400_BAD_REQUEST )

    def put(self, request, pk = None ):

        if(self.get_queryset(pk)):

            product_serializer = self.serializer_class( self.get_queryset(pk), data = request.data )

            if product_serializer.is_valid():

                product_serializer.save()

                return Response(product_serializer.data, status = status.HTTP_200_OK )
            
            return Response(product_serializer.errors, status = status.HTTP_400_BAD_REQUEST )

        return Response({'error':'No existe un producto con estso datos'}, status = status.HTTP_400_BAD_REQUEST )  

class CompanyDetailApiView(generics.RetrieveAPIView):

       queryset = Company.objects.all()
       serializer_class = CompanySerializer
       lookup_field = 'id'

@api_view(['GET','POST'])
def company_dbapi_view(request):

    if request.method == 'POST':

        data = request.data
        database_name = 'db_' + data['company']
        conn = psycopg2.connect(dbname='comun', user='postgres', password='Post1234', host='127.0.0.1')
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute('CREATE DATABASE ' + database_name)
        cursor.close()
        conn.close()
        # data['database_name'] = database_name
        # serializer = UserSerializer(data=data)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        return Response({'message':'base de datos creado'}, status=status.HTTP_201_CREATED)




class ModuleViewSet(viewsets.ModelViewSet):

    serializer_class = ModuleSerializer
    authentication_classes = [ Authentication ]
    # permission_classes = [permissions.IsAuthenticated, IsOwner]

    

    def get_queryset(self):

        return Module.objects.filter(usuario=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        module = serializer.save(usuario=request.user)

        # Crea la base de datos para la empresa
        db_name = f"{module.sigla}_{module.company.number}_2023"
        with connection.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE {db_name};")

        module.base_datos = db_name
        module.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class IdentityListApiView(generics.ListAPIView):

       serializer_class = IdentityDocumentSerializer
    #    authentication_classes = [Authentication]


       def get_queryset(self):
          

            model = self.get_serializer().Meta.model
            identitys = model.objects.all()

            return identitys
       
class DepartmentListApiView(generics.ListAPIView):

       serializer_class = DepartmentSerializer
       authentication_classes = [Authentication]


       def get_queryset(self):
          

            model = self.get_serializer().Meta.model
            departments = model.objects.all()

            return departments
       
class ProvinceListApiView(generics.ListAPIView):

       serializer_class = ProvincetSerializer
       authentication_classes = [Authentication]


       def get_queryset(self):
          

            model = self.get_serializer().Meta.model
            provinces = model.objects.all()

            return provinces
       
class DisctrictListApiView(generics.ListAPIView):


       serializer_class = DistrictSerializer
       authentication_classes = [Authentication]


       def get_queryset(self):
          

            model = self.get_serializer().Meta.model
            districts = model.objects.all()

            return districts
       
class ProviceDepartament(generics.ListAPIView):
      
      serializer_class = ProvincetSerializer

      def get_queryset(self):
            
            department = self.kwargs['department']
            model = self.get_serializer().Meta.model
            provices = model.objects.filter( department_id = department  )

            return provices
      
class DistrictProvince(generics.ListAPIView):
      
      serializer_class = DistrictSerializer

      def get_queryset(self):
            
            province = self.kwargs['province']
            model = self.get_serializer().Meta.model
            districts = model.objects.filter( province_id = province  )

            return districts
      
class ProvinceDetail(generics.RetrieveAPIView):
    
    queryset = Province.objects.all()
    serializer_class = ProvincetSerializer
    lookup_field = 'id'

class UnitViewSet(viewsets.ModelViewSet):

      queryset = Unit.objects.all()
      serializer_class = UnitSerializer

class CurrencyViewSet(viewsets.ModelViewSet):

      queryset = Currency.objects.all().order_by('-id')
      serializer_class = CurrencySerializer

class AffectationIgvViewSet(viewsets.ModelViewSet):

      queryset = AffectationIgv.objects.all()
      serializer_class = AffectationIgvSerializer

class DocumentTypeViewSet(viewsets.ModelViewSet):
     
     queryset = DocumentType.objects.all()
     serializer_class = DocumentTypeSerializer

class PaymentMethodTypeViewSet(viewsets.ModelViewSet):
     
     queryset = PaymentMethodType.objects.all()

class OperationTypeViewSet(viewsets.ModelViewSet):
     
     queryset = OperationType.objects.all()
     serializer_class = OperationTypeSerializer

class PaymentConditionViewSet(viewsets.ModelViewSet):
     
     queryset = PaymentCondition.objects.all()
     serializer_class = PaymentConditionSerializer







