from django.shortcuts import render
from rest_framework import viewsets
from .models import VehicleCountry
from .serializers import VehicleCountrySerializer
# Create your views here.
class VehicleCountryView(viewsets.ModelViewSet):
    queryset = VehicleCountry.objects.all()
    serializer_class = VehicleCountrySerializer