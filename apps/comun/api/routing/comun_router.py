from django.urls import path
from apps.comun.api.views.comun_view import *
from rest_framework import routers

router = routers.DefaultRouter()

router.register('module', ModuleViewSet , basename="lista modules")
router.register('igv', AffectationIgvViewSet, basename="lista igv")
router.register('currency', CurrencyViewSet , basename="lista currency" )
router.register('unit', UnitViewSet , basename="lista unit" )
router.register('document-type', DocumentTypeViewSet, basename="document view set")
router.register('payment-method', PaymentMethodTypeViewSet, basename="payment view set")
router.register('operation-type', OperationTypeViewSet, basename="operation view set")
router.register('payment-condition', PaymentConditionViewSet, basename="payment condition view set")

urlpatterns = [
    
    path('identity/listar/', IdentityListApiView.as_view(), name = "listar identitys" ),
    path('department/listar/', DepartmentListApiView.as_view(), name = "listar departmentos" ),
    path('province/listar/', ProvinceListApiView.as_view(), name = "listar provincias" ),
    path('province/<slug:id>/', ProvinceDetail.as_view(), name = "listar provincia detail" ),
    path('province/<slug:department>/listar/', ProviceDepartament.as_view(), name = "listar provincias departamento" ),
    path('district/<slug:province>/listar/', DistrictProvince.as_view(), name = "listar districts provincias" ),
    path('district/listar/', DisctrictListApiView.as_view(), name = "listar distritos" ),

]  + router.urls


# urlpatterns = 