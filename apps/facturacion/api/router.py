from rest_framework import routers
from django.urls import path
from .api import *

router = routers.DefaultRouter()

router.register('warehouse', WarehouseViewSet, basename="warehouse")
router.register('establishment', EstablishmentViewSet, basename="warehouse")

urlpatterns = [

    path('client/listar/', ClientCompanyApiView.as_view(), name = "listar clientes"),
    path('client/crear/', ClientCreateApiView.as_view(), name = "listar crear" ),
    path('client/update/<int:pk>/', ClientUpdateApiView.as_view(),  name = "client update" ),
    path('client/delete/<int:pk>/', ClientDestroyApiView.as_view(), name = 'client delete' ),

    path('initdata/', InitDataApiView.as_view(), name = 'init data'),

    path('item/crear/', ItemCreateApiView.as_view(), name = 'item crear'),
    path('item/list/', ItemListApiView.as_view(), name = 'item listar'),
    path('item/update/<int:pk>/', ItemUpdateApiView.as_view(), name = 'item update'),
    path('item/delete/<int:pk>/', ItemDeleteApiView.as_view(), name = 'item delete')

] + router.urls