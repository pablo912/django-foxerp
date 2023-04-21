from rest_framework.response import Response
from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.pagination import  PageNumberPagination
from rest_framework import filters
from apps.facturacion.models import *

from .serializers import *
from apps.users.authentication_mixins import Authentication
from apps.comun.api.serializers.comun_serializer import *
class PaginacionLarga(PageNumberPagination):

      page_size = 1
      page_size_query_param = 'page_size'

# CLIENT

class ClientCompanyApiView(generics.ListAPIView):

      
      serializer_class = ClientListSerializer
      filter_backends = [filters.SearchFilter]
      search_fields = ['name']
      pagination_class = PaginacionLarga
      # authentication_classes = [ Authentication ]

      def get_queryset(self):
            
            # company_id = self.kwargs['company_id']
            # user = self.request.user
            model = self.get_serializer().Meta.model
            clients = model.objects.filter(  state = True )

            return clients
            # return Response(clients, status = status.HTTP_200_OK )

class ClientCreateApiView(generics.CreateAPIView):
      
       serializer_class = ClientSerializer
       authentication_classes = [ Authentication ]


       def post(self,request):
             
            client_serializer = self.serializer_class( data = request.data )

            if client_serializer.is_valid():

                user = self.request.user 

                client_serializer.save(user = user )

                return Response(client_serializer.data, status = status.HTTP_201_CREATED )
             
            return Response(client_serializer.errors, status = status.HTTP_400_BAD_REQUEST )
       
class ClientUpdateApiView(generics.UpdateAPIView):

      serializer_class = ClientSerializer
      
      def get_queryset(self, pk):

            return self.get_serializer().Meta.model.objects.filter(id = pk).first()
      

      def put(self,request,pk = None):


            if self.get_queryset(pk):

                  client_serializer = self.serializer_class(self.get_queryset(pk), data = request.data )

                  if client_serializer.is_valid():

                        client_serializer.save()

                        return Response(client_serializer.data, status = status.HTTP_200_OK )
                  
                  return Response(client_serializer.errors, status = status.HTTP_400_BAD_REQUEST )
            
            return Response({'error':'No existe un cliente con estos datos'}, status = status.HTTP_400_BAD_REQUEST )

class ClientDestroyApiView(generics.DestroyAPIView):

      serializer_class = ClientSerializer

      def get_queryset(self):
            
            return self.get_serializer().Meta.model.objects.filter( state = True )
      
      def delete(self,request,pk):

            client = self.get_queryset().filter( id = pk ).first()

            if client:

                  client.state = False
                  client.save()

                  return Response({'message':'cliente elimiando'}, status = status.HTTP_200_OK )
            
            return Response({'error':'usuario no encontrado'}, status = status.HTTP_400_BAD_REQUEST )

class InitDataApiView(generics.CreateAPIView):
      
      serializer_class = ClientSerializer
      authentication_classes = [ Authentication ]


      def post(self,request):
            

            return Response({'message':'data cargada'}, status = status.HTTP_201_CREATED )

            # establishments = Establishment.objects.first()       

            # if not establishments:

            #       establishment = Establishment(

            #       description = "Principal",
            #       department_id = "15",
            #       province_id = "1501",
            #       district_id = "150101",
            #       address = "-",
            #       email = "-",
            #       code = "00",
            #       has_igv = True,
            #       created_date = "2023-01-12 11:41:21",
            #       modified_data = "2023-01-12 11:41:21",
            #       deleted_date = "2023-01-12 11:41:21"

            #       )   

            #       establishment.save()

            #       warehouse = Warehouse()
            #       warehouse.establishment = establishment
            #       warehouse.description = "principal"
            #       warehouse.created_date = "2023-01-12 11:41:21"
            #       warehouse.modified_data = "2023-01-12 11:41:21"
            #       warehouse.deleted_date = "2023-01-12 11:41:21"

            #       warehouse.save()

            #       return Response({'message':'data cargada'}, status = status.HTTP_201_CREATED )
            # else :

            #    return Response({'message':'prosiga'}, status = status.HTTP_201_CREATED )

# ITEM

class ItemListApiView(generics.ListAPIView):
      
      serializer_class = ItemListSerializer
      filter_backends = [filters.SearchFilter]
      search_fields = ['name']
      pagination_class = PaginacionLarga

      def get_queryset(self):
            
            model = self.get_serializer().Meta.model
            items = model.objects.filter( state = True )

            return items

class ItemCreateApiView(generics.CreateAPIView):

      serializer_class = ItemSerializer

      def post(self,request):

          item_serializer = self.serializer_class( data = request.data )

          if item_serializer.is_valid():
                
                item_serializer.save()

                return Response(item_serializer.data, status = status.HTTP_201_CREATED )
          
          return Response(item_serializer.errors, status = status.HTTP_400_BAD_REQUEST )

class ItemUpdateApiView(generics.UpdateAPIView):

      serializer_class = ItemListSerializer

      def get_queryset(self, pk):

            return self.get_serializer().Meta.model.objects.filter( id = pk  ).first()
      
      def put(self,request,pk = None):

            if self.get_queryset(pk):

                  item_serializer = self.serializer_class(self.get_queryset(pk), data = request.data )

                  if item_serializer.is_valid():

                        item_serializer.save()

                        return Response(item_serializer.data, status = status.HTTP_201_CREATED)
                  
                  return Response(item_serializer.errors, status = status.HTTP_400_BAD_REQUEST )
            
            return Response({'error':'No existe un producto con estos datos'}, status=status.HTTP_404_NOT_FOUND )

class ItemDeleteApiView(generics.DestroyAPIView):

      serializer_class = ItemSerializer

      def delete(self,request,pk):

            client = self.get_serializer().Meta.model.objects.filter( id = pk ).first()

            if client:

                  client.delete()

                  return Response({'message':'registro eliminado'}, status=status.HTTP_200_OK )
            
            return Response({'error':'registro no encontrado'}, status = status.HTTP_400_BAD_REQUEST )

class WarehouseViewSet(viewsets.ModelViewSet):

      queryset = Warehouse.objects.all()
      serializer_class = WarehouseSerializer


class EstablishmentViewSet(viewsets.ModelViewSet):

      queryset = Establishment.objects.all()
      serializer_class = EstablishmentSerializer


