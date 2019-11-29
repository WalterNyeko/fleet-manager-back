from django.shortcuts import render
from rest_framework import viewsets
from .models import VehicleModelCode
from .serializers import VehicleModelCodeSerializer
# Create your views here.
class VehicleModelCodeView(viewsets.ModelViewSet):
    queryset = VehicleModelCode.objects.all()
    serializer_class = VehicleModelCodeSerializer