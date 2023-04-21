from rest_framework import status 
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def contabilidad_api_view(request):

    if request.method == 'GET':

         return Response({"message":"contabilidad"}, status = status.HTTP_200_OK )
