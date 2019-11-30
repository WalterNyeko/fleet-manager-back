from rest_framework import viewsets
from .models import VehicleRentalPaymentStatus
from .serializers import VehicleRentalPaymentStatusSerializers

# Create your views here.
class VehicleRentalPaymentStatusView(viewsets.ModelViewSet):
    queryset = VehicleRentalPaymentStatus.objects.all()
    serializer_class = VehicleRentalPaymentStatusSerializers

