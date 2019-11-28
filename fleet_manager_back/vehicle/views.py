from rest_framework import viewsets
from .models import Vehicle
from .serializers import VehicleSerializer

# Create your views here.


class VehicleView(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer