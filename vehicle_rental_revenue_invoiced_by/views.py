from rest_framework import viewsets
from .models import VehicleRentalRevenueInvoicedBy
from .serializers import VehicleRentalRevenueInvoicedBySerializers

# Create your views here.
class VehicleRentalRevenueInvoicedByView(viewsets.ModelViewSet):
    queryset = VehicleRentalRevenueInvoicedBy.objects.all()
    serializer_class = VehicleRentalRevenueInvoicedBySerializers

