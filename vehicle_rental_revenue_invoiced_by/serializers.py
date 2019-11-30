from rest_framework import serializers
from .models import VehicleRentalRevenueInvoicedBy

class VehicleRentalRevenueInvoicedBySerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleRentalRevenueInvoicedBy
        fields = ('vehicle_rental_revenue_invoiced_by', 'created_on')
