from django.shortcuts import render
from rest_framework import viewsets
from .models import VehicleStatus
from .serializers import VehicleStatusSerializer
# Create your views here.
class VehicleStatusView(viewsets.ModelViewSet):
    queryset = VehicleStatus.objects.all()
    serializer_class = VehicleStatusSerializer