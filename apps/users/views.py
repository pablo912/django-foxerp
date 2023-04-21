import secrets

from django.contrib.sessions.models import Session
from django.contrib.auth import authenticate
from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import get_user_model


from datetime import datetime

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token


from apps.users.api.serializers import UserTokenSerializer, PasswordChangeSerializer
from apps.users.models import User

class Login(ObtainAuthToken):

    def post(self,request,*args,**kwargs):

        email = request.data.get('email')
        password = request.data.get('password')
        
        user = authenticate(request, email=email, password=password)
   
        if user is not None:

             if user.is_state:

                token,created = Token.objects.get_or_create( user = user )
                user_serializer = UserTokenSerializer(user)
                
                if user.email_verify:

                    if created:

                        return Response({

                                'token' : token.key,
                                'user' : user_serializer.data,
                                'message' : 'Iniciado de sesion exitoso'

                        }, status = status.HTTP_201_CREATED )
                    
                    else:

                        return Response({

                                'token' : token.key,
                                'user' : user_serializer.data,
                                'message' : 'Iniciado de sesion exitoso'

                        }, status = status.HTTP_201_CREATED )

                else:

                     return Response({'error':'Estimado usuario debe verificar su email'}, status = status.HTTP_406_NOT_ACCEPTABLE )
                       

             else:

                return Response({'error','Este usuario no puede iniciar sesion'}, status = status.HTTP_401_UNAUTHORIZED )
        
        else:

              return Response({'error':'Nombre de usuario o contraseña no validos'}, status = status.HTTP_400_BAD_REQUEST )      
 

class Logout( APIView ):


    def get(self,request,*args,**kwargs):

        try:

            token = request.GET.get('token')
            token = Token.objects.filter(key = token ).first()

            if token:

                user = token.user
                  
                all_sessions = Session.objects.filter(expire_date__gte = datetime.now())

                if all_sessions.exists():

                    for session in all_sessions:

                        session_data = session.get_decoded()

                        if user.id == int( session_data.get('_auth_user_id')):

                            session.delete()

                token.delete()
                
                session_message = 'Sesiones del usuario eliminado'
                token_message = 'Token eliminado'

                return Response({'token_message': token_message, 'session_message': session_message}, status = status.HTTP_200_OK )     

            return Response({'error':'No se ha encontrado un usuario con estas credenciales'}, status = status.HTTP_409_CONFLICT)           
        
        except:

            return Response({'error':'debe enviar el token en los params'}, status = status.HTTP_409_CONFLICT)


class Refresh( APIView):


    def get(self,request, *args, **kwargs):

        username = request.GET.get('username')

        try: 

            user_token = Token.objects.get(

                user = UserTokenSerializer().Meta.model.objects.filter(username = username ).first()

            )

            return Response({
                'token' : user_token.key
            })
        

        except: 

            return Response({

                'error' : 'credenciales enviadas incorrectas.'
                
            }, status = status.HTTP_400_BAD_REQUEST )

        
class PasswordResetView(APIView):


    def post(self, request):

        email = request.data.get('email')

        user = User.objects.filter(email = email).first()    

        if user:

            user.api_token = secrets.token_hex(16)
            user.save()

            form = PasswordResetForm(request.POST)

            subject = 'Recuperar contraseña'
            html_content  = render_to_string('password_reset_email.html', {'user': user} )        
            send_mail(subject, '', settings.EMAIL_HOST_USER, [ email ], html_message=html_content)
                
            return Response({'message':'Email enviado'},status=status.HTTP_200_OK)
      
            
        return Response({'error':'El email ingresado no existe'}, status = status.HTTP_400_BAD_REQUEST )
    


class ChangePasswordView(generics.UpdateAPIView):
    

    serializer_class = PasswordChangeSerializer
    model = User

    def get_object(self, queryset=None):
        
        email = self.request.data.get('email', None)
        
        return User.objects.get(email=email)

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()

        user_pass = self.get_object()

        self.object.api_token = None
   

        form = SetPasswordForm(user=self.object, data=request.data)

        if form.is_valid():

            self.object.save()
            form.save()
            return Response({"detail": "Contraseña actualizada con éxito."})
        else:
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)