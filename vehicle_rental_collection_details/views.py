from rest_framework import viewsets
from .models import VehicleRentalCollectionDetails
from .serializers import VehicleRentalCollectionDetailsSerializers

# Create your views here.
class VehicleRentalCollectionDetailsView(viewsets.ModelViewSet):
    queryset = VehicleRentalCollectionDetails.objects.all()
    serializer_class = VehicleRentalCollectionDetailsSerializers

