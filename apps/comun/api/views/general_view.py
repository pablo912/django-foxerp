from rest_framework.views import APIView
from rest_framework.response import Response
from apps.comun.models import CompanySchema, Domain, Company
from apps.comun.api.serializers.comun_serializer import CompanySerializer
from apps.facturacion.models import Establishment, Warehouse

class CompanyCreateSchemaApiView(APIView):


    def post(self, request ):

        data = request.data

        companySchema = CompanySchema.objects.filter( company = data['company'] ).first()
        
        company = Company.objects.filter( pk = data['company'] ).first()

        company_serializer = CompanySerializer( company )

        if not companySchema:
 
            tenant = CompanySchema(schema_name = f"{company.ruc}{data['period']}" ,
            state = True,
            company = company)
            tenant.save()

            domain = Domain()
            domain.domain = f"{company.ruc}{data['period']}.localhost" # don't add your port or www here!
            domain.tenant = tenant
            domain.is_primary = True
            domain.save()

    
            return Response(company_serializer.data)
        
        else:


            return Response(company_serializer.data)


