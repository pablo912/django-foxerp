
from rest_framework.response import Response
from rest_framework import status, viewsets
from apps.comun.api.serializers.comun_serializer import ModuleSerializer    
from django_tenants.utils import get_tenant_model

class ClienteViewSet(viewsets.ModelViewSet):

    queryset = get_tenant_model().objects.all()
    serializer_class = ModuleSerializer