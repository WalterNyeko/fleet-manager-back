from django.shortcuts import render
from rest_framework import viewsets
from .models import VehicleCounty
from .serializers import VehicleCountySerializer
# Create your views here.
class VehicleCountyView(viewsets.ModelViewSet):
    queryset = VehicleCounty.objects.all()
    serializer_class = VehicleCountySerializer