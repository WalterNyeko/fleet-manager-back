from django.shortcuts import render
from rest_framework import viewsets
from .models import VehicleCurrencyCodes
from .serializers import VehicleCurrencyCodesSerializer
# Create your views here.
class VehicleCurrencyCodesView(viewsets.ModelViewSet):
    queryset = VehicleCurrencyCodes.objects.all()
    serializer_class = VehicleCurrencyCodesSerializer