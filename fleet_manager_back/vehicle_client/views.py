from django.shortcuts import render
from rest_framework import viewsets
from .models import VehicleClient
from .serializers import VehicleClientSerializer
# Create your views here.
class VehicleClientView(viewsets.ModelViewSet):
    queryset = VehicleClient.objects.all()
    serializer_class = VehicleClientSerializer