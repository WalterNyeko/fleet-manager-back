from django.shortcuts import render
from rest_framework import viewsets
from .models import VehicleReturnedWorkshop
from .serializers import VehicleReturnedWorkshopSerializer
# Create your views here.
class VehicleReturnedWorkshopView(viewsets.ModelViewSet):
    queryset = VehicleReturnedWorkshop.objects.all()
    serializer_class = VehicleReturnedWorkshopSerializer