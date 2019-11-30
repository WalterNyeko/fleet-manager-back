from django.shortcuts import render
from rest_framework import viewsets
from .models import VehicleDeductability
from .serializers import VehicleDeductabilitySerializer
# Create your views here.
class VehicleDeductabilityView(viewsets.ModelViewSet):
    queryset = VehicleDeductability.objects.all()
    serializer_class = VehicleDeductabilitySerializer