from django.contrib import admin
from django.urls import path, include
from apps.contabilidad.api.api import *
from rest_framework.authtoken import views
from apps.users.views import Login, Logout, Refresh, PasswordResetView, ChangePasswordView


urlpatterns = [
    

    path('facturacion/', include('apps.facturacion.api.router')),
    path('contabilidad/', include('apps.contabilidad.api.routes')),

  

    # path('planilla/', include('apps.planilla.api.api') ),

]
