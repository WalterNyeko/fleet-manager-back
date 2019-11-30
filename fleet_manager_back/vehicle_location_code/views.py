from django.shortcuts import render
from rest_framework import viewsets
from .models import VehicleLocationCode
from .serializers import VehicleLocationCodeSerializer
# Create your views here.
class VehicleLocationCodeView(viewsets.ModelViewSet):
    queryset = VehicleLocationCode.objects.all()
    serializer_class = VehicleLocationCodeSerializer