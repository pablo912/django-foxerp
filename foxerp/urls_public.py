from django.contrib import admin
from django.urls import path, include
from apps.contabilidad.api.api import *
from rest_framework.authtoken import views
from apps.users.views import Login, Logout, Refresh, PasswordResetView, ChangePasswordView


urlpatterns = [
    
    path("admin/", admin.site.urls),
    path('company/', include('apps.comun.api.routing.general_router')),
    path('comun/', include('apps.comun.api.routing.comun_router')),

    path('api-token-auth/', views.obtain_auth_token),
    path('', Login.as_view(), name = "login"),
    path('logout/', Logout.as_view(), name = "logout"),
    path('users/', include('apps.users.api.router')),
    path('refresh-token', Refresh.as_view(), name = "refresh" ),
    path('password/reset/', PasswordResetView.as_view(), name='password_reset'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
  

    # path('planilla/', include('apps.planilla.api.api') ),

]
