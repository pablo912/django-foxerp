from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


from apps.users.models import User
from apps.users.authentication_mixins import Authentication
from apps.users.api.serializers import UserSerializer, UserListSerializer, UserByAdminSerializer


from rest_framework import generics, status 
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.views import APIView




class ListUserByAdminApiView(generics.ListAPIView):

    serializer_class = UserByAdminSerializer
    authentication_classes = [ Authentication ]

    def get_queryset(self):
        
        user = self.request.user
        
        model = self.get_serializer().Meta.model
        return model.objects.filter( created_by = user.id  )


class UserByAdminCreateApiView(generics.CreateAPIView):

    serializer_class = UserByAdminSerializer
    authentication_classes = [ Authentication ]


    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():

            user = serializer.save()

            user.is_active = True
            user.is_admin = False
            user.email_verify = True
            user.created_by = self.request.user
            user.save()


            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)


class MyView(APIView):

    authentication_classes = [Authentication]


    def get(self, request, format=None):
        # aquí puede acceder al usuario autenticado a través de la solicitud (request)
        user = request.user
        
        user_serializer = UserSerializer(user)

        return Response(user_serializer.data, status=status.HTTP_200_OK )


@api_view(['GET'])
def user_api_token_verify(request,token = None ):

    user = User.objects.filter(api_token = token).first()

    user_serilizer = UserSerializer(user)

    if user:
         
            return Response({'message':'existe el usuario','user':user_serilizer.data  }, status = status.HTTP_200_OK)
    
    else:
         
        return Response({'error':'credenciales no validos'}, status = status.HTTP_409_CONFLICT )


@api_view(['GET'])
def user_api_verify(request,token = None ):

    user = User.objects.filter(api_token_email = token).first()    

    if user:
         
        if request.method == 'GET':          

            user.email_verify = True
            user.api_token_email = None
            user.save()

            return Response({'message':'email verificado'}, status = status.HTTP_200_OK)
    
    else:
         
        return Response({'error':'credenciales no validos'}, status = status.HTTP_409_CONFLICT )

@api_view(['GET','POST'])
def user_api_view(request):
    
    if request.method == 'GET':

        users = User.objects.all().values('id','username','email','password')
        users_serializer = UserListSerializer(users, many = True)
        return Response(users_serializer.data, status = status.HTTP_200_OK)
    

    elif request.method == 'POST':

        print(request.data)

        user_serializer = UserSerializer( data = request.data )

  
    
        if user_serializer.is_valid():

            user = user_serializer.save()
        
            subject = 'Verifica tu correo electrónico'
            html_content  = render_to_string('email_verification.html', {'user': user})        
            send_mail(subject, '', settings.EMAIL_HOST_USER, [user.email ], html_message=html_content)

            return Response({"message":"Usuario creado"}, status = status.HTTP_201_CREATED )
        
        return Response(user_serializer.errors, status = status.HTTP_400_BAD_REQUEST )
    
    
@api_view(['GET','PUT','DELETE'])
def user_detail_api_view(request,pk=None):

    user = User.objects.filter(id = pk).first()

    if user:

        if request.method == 'GET':

            user_serializer = UserSerializer(user)

            return Response(user_serializer.data, status = status.HTTP_200_OK)   
        
        elif request.method == 'PUT':

            user_serializer = UserSerializer(user, data = request.data )

            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status = status.HTTP_200_OK)
            
            return Response(user_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'DELETE':

            user.delete()
            return Response({"message":"Eliminado"}, status = status.HTTP_200_OK )

    return Response({"message":"El usuario con este id no existe"}, status=status.HTTP_404_NOT_FOUND)


@authentication_classes([Authentication])
@api_view(['GET'])
def user_me(request):

    if request.method == 'GET':

        user = request.user

        if user:

            user_serializer = UserSerializer(user)

            return Response(user_serializer.data, status = status.HTTP_200_OK)   
        
        return Response({'error':'usuario no encontrado'}, status = status.HTTP_404_NOT_FOUND)   

