from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from vehicle.views import (
    VehicleInsuranceCompanyView,
    VehicleView,
    VehicleBodyTypeView,
    VehicleClientView,
    VehicleCompanyCodeView,
    VehicleConventionTypeView,
    VehicleCountyView,
    VehicleCountryView,
    VehicleCostCenterView,
    VehicleCurrencyCodesView,
    VehicleDeductabilityView,
    VehicleFuelTypeView,
    VehicleGearBoxView,
    VehicleInPullView,
    VehicleLocationCodeView,
    VehicleMakeCodeView,
    VehicleModelCodeView,
    VehicleReturnedWorkshopView,
    VehicleStatusView,
    VehicleTypeView,
    VehicleTyreView,
    VehicleSummaryView,
    VehicleBasicView,
    VehicleDiaryView,
    VehicleInsuranceCompanyView,
    VehicleAllocationView,
    VehicleAssetsView,
    VehicleComponentsView,
)

# Serializers define the API representation.


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "is_staff"]


# ViewSets define the view behavior.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"vehicles", VehicleView)
router.register(r"vehicleclient", VehicleClientView)
router.register(r"vehiclebodytypes", VehicleBodyTypeView)
router.register(r"vehiclecompanycode", VehicleCompanyCodeView)
router.register(r"vehicleconventiontype", VehicleConventionTypeView)
router.register(r"vehiclecostcenter", VehicleCostCenterView)
router.register(r"vehiclecounty", VehicleCountyView)
router.register(r"vehiclecountry", VehicleCountryView)
router.register(r"vehiclecurrencycodes", VehicleCurrencyCodesView)
router.register(r"vehicledeductability", VehicleDeductabilityView)
router.register(r"vehiclefueltype", VehicleFuelTypeView)
router.register(r"vehiclegearbox", VehicleGearBoxView)
router.register(r"vehicleinpull", VehicleInPullView)
router.register(r"vehiclelocationcode", VehicleLocationCodeView)
router.register(r"vehiclemakecode", VehicleMakeCodeView)
router.register(r"vehiclemodelcode", VehicleModelCodeView)
router.register(r"vehiclereturnedworkshop", VehicleReturnedWorkshopView)
router.register(r"vehiclestatus", VehicleStatusView)
router.register(r"vehicletypes", VehicleTypeView)
router.register(r"vehicletyres", VehicleTyreView)
router.register(r"vehiclesummary", VehicleSummaryView)
router.register(r"vehicleinsurancecompany", VehicleInsuranceCompanyView)
router.register(r"vehiclebasic", VehicleBasicView)
router.register(r"vehiclediary", VehicleDiaryView)
router.register(r"vehicleinsurancecompany", VehicleInsuranceCompanyView)
router.register(r"vehicleallocation", VehicleAllocationView)
router.register(r"vehicleallocation", VehicleAssetsView)
router.register(r"vehiclecomponents", VehicleComponentsView)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^", include(router.urls)),
    url(r"^api-auth/", include("rest_framework.urls", namespace="home")),
]
