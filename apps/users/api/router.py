from django.urls import path
from apps.users.api.api import *


urlpatterns = [
    path('usuario/', user_api_view, name="user api"),
    path('usuario/<int:pk>/', user_detail_api_view, name="usuario detail"),
    path('usuario/verify-email/<slug:token>', user_api_verify, name = "email verify "),
    path('usuario/verify-token/<slug:token>', user_api_token_verify, name = "token verify "),
    path('usuario/secundario/crear', UserByAdminCreateApiView.as_view(), name="user secundario"),
    path('usuario/secundario/list', ListUserByAdminApiView.as_view(), name="user secundario list"),
    path('usuario/secundario/list', ListUserByAdminApiView.as_view(), name="user secundario list"),
    path('me', MyView.as_view(), name = "user me")

]