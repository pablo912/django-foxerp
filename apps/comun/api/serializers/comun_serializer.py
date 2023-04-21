from apps.comun.models import *
from rest_framework import serializers
from apps.users.models import User 


class ModuleSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Module
        fields = '__all__'

class IdentityDocumentSerializer(serializers.ModelSerializer):

      class Meta:
          
          model = IdentityDocument
          fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    
      class Meta:
          
         model = Department
         fields = '__all__'


class ProvincetSerializer(serializers.ModelSerializer):
    
      class Meta:
          
         model = Province
         fields = '__all__'


class DistrictSerializer(serializers.ModelSerializer):
    
      class Meta:
          
         model = District
         fields = '__all__'



class CompanySerializer(serializers.ModelSerializer):
 
    class Meta:
      
      model = Company
      fields = '__all__'
      # exclude = ('state',)

    
    def to_representation(self,instance):
       
       return {
          
          'id' : instance.id,
          'ruc' : instance.ruc,
          'name' : instance.name,
          'direction' : instance.direction,
          'email' : instance.email if instance.email != '' else '',
          'user' : instance.user.name,
          'state' : instance.state

       }




class UnitSerializer(serializers.ModelSerializer):

    class Meta:

        model = Unit
        fields = '__all__'


class CurrencySerializer(serializers.ModelSerializer):

    class Meta:

        model = Currency
        fields = '__all__'

class AffectationIgvSerializer(serializers.ModelSerializer):


    class Meta:

        model = AffectationIgv
        fields = '__all__'


class DocumentTypeSerializer(serializers.ModelSerializer):

    class Meta:

        model = DocumentType
        fields = '__all__'

class PaymentMethodTypeSerializer(serializers.ModelSerializer):

    class Meta:

        model = PaymentMethodType
        fields = '__all__'
    
class OperationTypeSerializer(serializers.ModelSerializer):

    class Meta:

        model = OperationType
        fields = '__all__'

class PaymentConditionSerializer(serializers.ModelSerializer):

    class Meta:

        model = PaymentCondition
        fields = '__all__'