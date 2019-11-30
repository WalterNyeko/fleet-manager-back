from rest_framework import serializers
from .models import Vehicle
from vehicle_tyre.serializers import VehicleTyreSerializer
from vehicle_body_type.serializers import VehicleBodyTypeSerializer
from vehicle_client.serializers import VehicleClientSerializer
from vehicle_company_code.serializers import VehicleCompanyCodeSerializer
from vehicle_convention_type.serializers import VehicleConventionTypeSerializer
from vehicle_cost_center.serializers import VehicleCostCenterSerializer
from vehicle_country.serializers import VehicleCountrySerializer
from vehicle_fuel_type.serializers import VehicleFuelTypeSerializer
from vehicle_make_code.serializers import VehicleMakeCodeSerializer
from vehicle_model_code.serializers import VehicleModelCodeSerializer
from vehicle_returned_workshop.serializers import VehicleReturnedWorkshopSerializer
from vehicle_status.serializers import VehicleStatusSerializer
from vehicle_county.serializers import VehicleCountySerializer


class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    vehicle_tyre = VehicleTyreSerializer(many=False, read_only=True)
    vehicle_body_type = VehicleBodyTypeSerializer(many=False, read_only=True)
    vehicle_client = VehicleClientSerializer(many=False, read_only=True)
    vehicle_company_code = VehicleCompanyCodeSerializer(many=False, read_only=True)
    vehicle_convention_type = VehicleConventionTypeSerializer(many=False, read_only=True)
    vehicle_cost_center = VehicleCostCenterSerializer(many=False, read_only=True)
    vehicle_country = VehicleCountrySerializer(many=False, read_only=True)
    vehicle_fuel_type = VehicleFuelTypeSerializer(many=False, read_only=True)
    vehicle_make_code = VehicleMakeCodeSerializer(many=False, read_only=True)
    vehicle_model_code = VehicleModelCodeSerializer(many=False, read_only=True)
    vehicle_returned_workshop = VehicleReturnedWorkshopSerializer(many=False, read_only=True)
    vehicle_status = VehicleStatusSerializer(many=False, read_only=True)
    vehicle_county = VehicleCountySerializer(many=False, read_only=True)
    class Meta:
        model = Vehicle
        fields = ('registration_no','extra_registration_no','year','fleet_number','date_registered','date_returned_to_workshop', 'vehicle_tyre', 'vehicle_body_type', 'vehicle_client', 'vehicle_company_code', 'vehicle_convention_type', 'vehicle_cost_center', 'vehicle_country', 'vehicle_fuel_type', 'vehicle_make_code', 'vehicle_model_code', 'vehicle_returned_workshop', 'vehicle_status', 'vehicle-county')
