from rest_framework import viewsets
from .models import VehicleHireStatus
from .serializers import VehicleHireStatusSerializers

# Create your views here.
class VehicleHireStatusView(viewsets.ModelViewSet):
    queryset = VehicleHireStatus.objects.all()
    serializer_class = VehicleHireStatusSerializers

