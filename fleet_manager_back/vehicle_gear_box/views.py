from django.shortcuts import render
from rest_framework import viewsets
from .models import VehicleGearBox
from .serializers import VehicleGearBoxSerializer
# Create your views here.
class VehicleGearBoxView(viewsets.ModelViewSet):
    queryset = VehicleGearBox.objects.all()
    serializer_class = VehicleGearBoxSerializer