from rest_framework import viewsets
from .models import VehicleHire,VehicleHireRentalCollectionDetails,VehicleHireRentalRevenue,VehicleHireRentalStatus, VehicleHireCostCenter,VehicleHireReason, VehicleHireStatus,VehicleHireRentalDetailHiringDivision, VehicleHireRentalInvoicesTo, VehicleHireRentalPaymentRecievedBy, VehicleHireRentalPaymentStatus,VehicleHireRentalRevenueInvoicedBy,VehicleHireRentalPaymentRecieved
from .serializers import (
    VehicleHireSerializers,
    VehicleHireRentalRevenueSerializers, 
    VehicleHireCostCenterSerializers, 
    VehicleHireReasonSerializers, 
    VehicleHireRentalStatusSerializers,
    VehicleHireStatusSerializers,
    VehicleHireRentalDetailHiringDivisionSerializers,
    VehicleHireRentalInvoicesToSerializers,
    VehicleHireRentalPaymentRecievedSerializers,
    VehicleHireRentalPaymentRecievedBySerializers,
    VehicleHireRentalPaymentStatusSerializers,
    VehicleHireRentalCollectionDetailsSerializers,
    VehicleHireRentalRevenueInvoicedBySerializers)

# Create your views here.
class VehicleHireRentalRevenueView(viewsets.ModelViewSet):
    queryset = VehicleHireRentalRevenue.objects.all()
    serializer_class = VehicleHireRentalRevenueSerializers
    

class VehicleHireRentalCollectionDetailsView(viewsets.ModelViewSet):
    queryset = VehicleHireRentalCollectionDetails.objects.all()
    serializer_class = VehicleHireRentalCollectionDetailsSerializers    
    

class VehicleHireRentalRevenueInvoicedByView(viewsets.ModelViewSet):
    queryset = VehicleHireRentalRevenueInvoicedBy.objects.all()
    serializer_class = VehicleHireRentalRevenueInvoicedBySerializers

class VehicleHireRentalPaymentStatusView(viewsets.ModelViewSet):
    queryset = VehicleHireRentalPaymentStatus.objects.all()
    serializer_class = VehicleHireRentalPaymentStatusSerializers

class VehicleHireRentalPaymentRecievedByView(viewsets.ModelViewSet):
    queryset = VehicleHireRentalPaymentRecievedBy.objects.all()
    serializer_class = VehicleHireRentalPaymentRecievedBySerializers

class VehicleHireRentalPaymentRecievedView(viewsets.ModelViewSet):
    queryset = VehicleHireRentalPaymentRecieved.objects.all()
    serializer_class = VehicleHireRentalPaymentRecievedSerializers

class VehicleHireRentalInvoicesToView(viewsets.ModelViewSet):
    queryset = VehicleHireRentalInvoicesTo.objects.all()
    serializer_class = VehicleHireRentalInvoicesToSerializers

class VehicleHireRentalDetailHiringDivisionView(viewsets.ModelViewSet):
    queryset = VehicleHireRentalDetailHiringDivision.objects.all()
    serializer_class = VehicleHireRentalDetailHiringDivisionSerializers

class VehicleHireStatusView(viewsets.ModelViewSet):
    queryset = VehicleHireStatus.objects.all()
    serializer_class = VehicleHireStatusSerializers


class VehicleHireRentalStatusView(viewsets.ModelViewSet):
     queryset = VehicleHireRentalStatus.objects.all()
     serializer_class = VehicleHireRentalStatusSerializers

class VehicleHireReasonView(viewsets.ModelViewSet):
        queryset = VehicleHireReason.objects.all()
        serializer_class = VehicleHireReasonSerializers

class VehicleHireCostCenterView(viewsets.ModelViewSet):
    queryset = VehicleHireCostCenter.objects.all()
    serializer_class = VehicleHireCostCenterSerializers

class VehicleHireView(viewsets.ModelViewSet):
    queryset = VehicleHire.objects.all()
    serializer_class = VehicleHireSerializers
