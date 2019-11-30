from rest_framework import serializers
from .models import VehicleCurrencyCodes


class VehicleCurrencyCodesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleCurrencyCodes
        fields = ("currency_codes_name", "created_on")

