from django.shortcuts import render
from rest_framework import viewsets
from .models import VehicleFuelType
from .serializers import VehicleFuelTypeSerializer
# Create your views here.
class VehicleFuelTypeView(viewsets.ModelViewSet):
    queryset = VehicleFuelType.objects.all()
    serializer_class = VehicleFuelTypeSerializer