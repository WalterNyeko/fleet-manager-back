from rest_framework import viewsets
from .models import VehicleRentalPaymentRecievedBy
from .serializers import VehicleRentalPaymentRecievedBySerializers

# Create your views here.
class VehicleRentalPaymentRecievedByView(viewsets.ModelViewSet):
    queryset = VehicleRentalPaymentRecievedBy.objects.all()
    serializer_class = VehicleRentalPaymentRecievedBySerializers

