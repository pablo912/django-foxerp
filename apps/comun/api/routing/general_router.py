from django.urls import path
from apps.comun.api.views.comun_view import *
from apps.comun.api.views.general_view import CompanyCreateSchemaApiView

urlpatterns = [
    
  
    path('company/listar/', CompanyListApiView.as_view(), name="products"),
    path('company/crear/', CompanyCrateApiView.as_view(), name = "product crear" ),
    path('company/<int:id>/', CompanyDetailApiView.as_view(), name = "product detail" ),
    path('company/update/<int:pk>/', CompanyDetailApiView.as_view(), name = "product update " ),
    path('schema/crear/', CompanyCreateSchemaApiView.as_view(), name = "schema create "),


]   