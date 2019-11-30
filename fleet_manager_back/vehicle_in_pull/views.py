from django.shortcuts import render
from rest_framework import viewsets
from .models import VehicleInPull
from .serializers import VehicleInPullSerializer
# Create your views here.
class VehicleInPullView(viewsets.ModelViewSet):
    queryset = VehicleInPull.objects.all()
    serializer_class = VehicleInPullSerializer