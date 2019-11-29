from django.shortcuts import render
from rest_framework import viewsets
from .models import VehicleConventionType
from .serializers import VehicleConventionTypeSerializer
# Create your views here.
class VehicleConventionTypeView(viewsets.ModelViewSet):
    queryset = VehicleConventionType.objects.all()
    serializer_class = VehicleConventionTypeSerializer