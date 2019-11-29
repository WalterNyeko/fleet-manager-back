from django.shortcuts import render
from rest_framework import viewsets
from .models import VehicleCostCenter
from .serializers import VehicleCostCenterSerializer
# Create your views here.
class VehicleCostCenterView(viewsets.ModelViewSet):
    queryset = VehicleCostCenter.objects.all()
    serializer_class = VehicleCostCenterSerializer