from rest_framework import viewsets
from .models import VehicleHireRentalStatus
from .serializers import VehicleHireRentalStatusSerializers

# Create your views here.
class VehicleHireRentalStatusView(viewsets.ModelViewSet):
     queryset = VehicleHireRentalStatus.objects.all()
     serializer_class = VehicleHireRentalStatusSerializers


