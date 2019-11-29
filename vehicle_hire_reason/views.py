from rest_framework import viewsets
from .models import VehicleHireReason
from .serializers import VehicleHireReasonSerializers

# Create your views here.
class VehicleHireReasonView(viewsets.ModelViewSet):
        queryset = VehicleHireReason.objects.all()
        serializer_class = VehicleHireReasonSerializers



