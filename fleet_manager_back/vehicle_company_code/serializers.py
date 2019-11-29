from rest_framework import serializers
from .models import VehicleCompanyCode

class VehicleCompanyCodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleCompanyCode
        fields = ('company_code_name','created_on')