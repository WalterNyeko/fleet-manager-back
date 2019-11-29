from django.shortcuts import render
from rest_framework import viewsets
from .models import VehicleBodyType
from .serializers import VehicleBodyTypeSerializer
# Create your views here.
class VehicleBodyTypeView(viewsets.ModelViewSet):
    queryset = VehicleBodyType.objects.all()
    serializer_class = VehicleBodyTypeSerializer