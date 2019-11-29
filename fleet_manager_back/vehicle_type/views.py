from django.shortcuts import render
from rest_framework import viewsets
from .models import VehicleType
from .serializers import VehicleTypeSerializer
# Create your views here.
class VehicleTypeView(viewsets.ModelViewSet):
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer