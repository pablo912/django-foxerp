from django.urls import path
from apps.contabilidad.api.api import contabilidad_api_view


urlpatterns = [
    path('', contabilidad_api_view),

]