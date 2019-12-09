from rest_framework import serializers
from .models import VehicleHire,VehicleHireRentalCollectionDetails,VehicleHireRentalRevenue,VehicleHireCostCenter,VehicleHireReason,VehicleHireRentalStatus,VehicleHireStatus,VehicleHireRentalDetailHiringDivision,VehicleHireRentalInvoicesTo, VehicleHireRentalPaymentRecieved, VehicleHireRentalPaymentRecievedBy,VehicleHireRentalPaymentStatus, VehicleHireRentalRevenueInvoicedBy

class VehicleHireRentalRevenueSerializers(serializers.ModelSerializer):
    class Meta:
        model = VehicleHireRentalRevenue
        fields = '__all__'

class VehicleHireRentalRevenueInvoicedBySerializers(serializers.ModelSerializer):
    class Meta:
        model = VehicleHireRentalRevenueInvoicedBy
        fields = '__all__'

class VehicleHireRentalPaymentStatusSerializers(serializers.ModelSerializer):
    class Meta:
        model = VehicleHireRentalPaymentStatus
        fields = '__all__'

class VehicleHireRentalPaymentRecievedBySerializers(serializers.ModelSerializer):
    class Meta:
        model = VehicleHireRentalPaymentRecievedBy
        fields = '__all__'

class VehicleHireRentalPaymentRecievedSerializers(serializers.ModelSerializer):
    class Meta:
        model = VehicleHireRentalPaymentRecieved
        fields = '__all__'
        
class VehicleHireRentalInvoicesToSerializers(serializers.ModelSerializer):
    class Meta:
        model = VehicleHireRentalInvoicesTo
        fields = '__all__'

class VehicleHireRentalDetailHiringDivisionSerializers(serializers.ModelSerializer):
    class Meta:
        model = VehicleHireRentalDetailHiringDivision
        fields = '__all__'

class VehicleHireRentalCollectionDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = VehicleHireRentalCollectionDetails
        fields = '__all__'

class VehicleHireStatusSerializers(serializers.ModelSerializer):
    class Meta:
        model = VehicleHireStatus
        fields = '__all__'

class VehicleHireRentalStatusSerializers(serializers.ModelSerializer):
    class Meta:
        model = VehicleHireRentalStatus
        fields = '__all__'

class VehicleHireReasonSerializers(serializers.ModelSerializer):
    class Meta:
        model = VehicleHireReason
        fields = '__all__'

class VehicleHireCostCenterSerializers(serializers.ModelSerializer):
    class Meta:
        model = VehicleHireCostCenter
        fields = '__all__'

class VehicleHireSerializers(serializers.ModelSerializer):
    class Meta:
        model = VehicleHire
        fields = '__all__'