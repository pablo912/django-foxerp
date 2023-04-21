from django.db import connection
from apps.comun.models import Equipo

class SeleccionarEquipoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        equipo_nombre = request.headers.get('Equipo')
        if equipo_nombre:
            try:
                equipo = Equipo.objects.get(nombre=equipo_nombre)
                connection.set_schema(equipo.esquema_bd)
            except Equipo.DoesNotExist:
                pass
        response = self.get_response(request)
        return response