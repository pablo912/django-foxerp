from rest_framework import serializers
from apps.facturacion.models import *


class ClientListSerializer(serializers.ModelSerializer):

    class Meta:

        model = Client
        fields = '__all__'

    def to_representation(self, instance):

        print(instance)

        return {

            'id' : instance.id,
            'identity_document_type' : instance.identity_document_type.description,
            'identity_document_type_id' : instance.identity_document_type.id,   
            'name' : instance.name,
            'number' : instance.number,
            'type' : instance.type,
            'trade_name' : instance.trade_name,
            'address' : instance.address,
            'state' : instance.state,
            'department' : instance.department.id if instance.department != None else None,
            'province' : instance.province.id if instance.province != None else None,
            'district' : instance.district.id if instance.district != None else None,
            'email' : instance.email,
            'phone' : instance.phone
        }
        
class ClientSerializer(serializers.ModelSerializer):

    class Meta:

        model = Client
        fields = '__all__'

class ItemListSerializer(serializers.ModelSerializer):

    class Meta:

       model = Item
       fields = '__all__'

    def to_representation(self,intance):

        return {

            'id' : intance.id,
            'has_igv': intance.has_igv,
            'name' : intance.name,
            'price' : intance.price,
            'stock' : intance.stock,
            'currency' :  intance.currency.id,
            'item_type' : intance.item_type.description,
            'item_type_id' : intance.item_type.id,
            'affectation_igv' : intance.affectation_igv.description,
            'affectation_igv_id' : intance.affectation_igv.id,
            'unit' : intance.unit.description,
            'unit_id' : intance.unit.id,
            "calculate_quantity": intance.calculate_quantity,
            "has_plastic_tax": intance.has_plastic_tax,   
            "description" : intance.description,
            "model" : intance.model,
            'stock_min' : intance.stock_min,
            'date_of_due' : intance.date_of_due,
            'warehouse' : intance.warehouse.id,
            'itemcode' : intance.itemcode,
            'sunatcode' : intance.sunatcode,

        }    

class ItemSerializer(serializers.ModelSerializer):

    class Meta:

        model = Item
        fields = '__all__'

class WarehouseSerializer(serializers.ModelSerializer):

    class Meta:

        model = Warehouse
        fields = '__all__'

class EstablishmentSerializer(serializers.ModelSerializer):

    class Meta:

        model = Establishment
        fields = '__all__'

class SerieSerializer(serializers.ModelSerializer):

    class Meta:

        model = Serie
        fields = '__all__'

        