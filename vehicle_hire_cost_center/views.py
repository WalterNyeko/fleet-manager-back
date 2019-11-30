from rest_framework import viewsets
from .models import VehicleHireCostCenter
from .serializers import VehicleHireCostCenterSerializrs

# Create your views here.
class VehicleHireCostCenterView(viewsets.ModelViewSet):
    queryset = VehicleHireCostCenter.objects.all()
    serializer_class = VehicleHireCostCenterSerializrs