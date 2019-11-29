from django.shortcuts import render
from rest_framework import viewsets
from .models import VehicleMakeCode
from .serializers import VehicleMakeCodeSerializer
# Create your views here.
class VehicleMakeCodeView(viewsets.ModelViewSet):
    queryset = VehicleMakeCode.objects.all()
    serializer_class = VehicleMakeCodeSerializer