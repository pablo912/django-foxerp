from django.contrib import admin
from apps.comun.models import *
from django_tenants.admin import TenantAdminMixin


@admin.register(Company)
class CompanyAdmin(TenantAdminMixin, admin.ModelAdmin):
        list_display = ('ruc',)



admin.site.register(Module)