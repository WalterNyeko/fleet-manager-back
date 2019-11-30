from rest_framework import viewsets
from .models import VehicleRentalDetailHiringDivision
from .serializers import VehicleRentalDetailHiringDivisionSerializers

# Create your views here.
class VehicleRentalDetailHiringDivisionView(viewsets.ModelViewSet):
    queryset = VehicleRentalDetailHiringDivision.objects.all()
    serializer_class = VehicleRentalDetailHiringDivisionSerializers

