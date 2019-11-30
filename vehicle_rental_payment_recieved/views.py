from rest_framework import viewsets
from .models import VehicleRentalPaymentRecieved
from .serializers import VehicleRentalPaymentRecievedSerializers

# Create your views here.
class VehicleRentalPaymentRecievedView(viewsets.ModelViewSet):
    queryset = VehicleRentalPaymentRecieved.objects.all()
    serializer_class = VehicleRentalPaymentRecievedSerializers

