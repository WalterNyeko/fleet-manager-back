from django.shortcuts import render
from rest_framework import viewsets
from .models import VehicleCompanyCode
from .serializers import VehicleCompanyCodeSerializer
# Create your views here.
class VehicleCompanyCodeView(viewsets.ModelViewSet):
    queryset = VehicleCompanyCode.objects.all()
    serializer_class = VehicleCompanyCodeSerializer