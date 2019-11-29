from django.shortcuts import render
from rest_framework import viewsets
from .models import VehicleTyre
from .serializers import VehicleTyreSerializer
# Create your views here.
class VehicleTyreView(viewsets.ModelViewSet):
    queryset = VehicleTyre.objects.all()
    serializer_class = VehicleTyreSerializer