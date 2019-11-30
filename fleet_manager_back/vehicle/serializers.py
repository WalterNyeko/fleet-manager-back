from rest_framework import serializers
from .models import (
    VehicleInsuranceCompany,
    VehicleSummary,
    Vehicle,
    VehicleClient,
    VehicleBodyType,
    VehicleCompanyCode,
    VehicleConventionType,
    VehicleCostCenter,
    VehicleCountry,
    VehicleCounty,
    VehicleCurrencyCodes,
    VehicleDeductability,
    VehicleFuelType,
    VehicleGearBox,
    VehicleInPull,
    VehicleLocationCode,
    VehicleMakeCode,
    VehicleModelCode,
    VehicleReturnedWorkshop,
    VehicleStatus,
    VehicleType,
    VehicleTyre,
    VehicleBasic,
    VehicleDiary,
    VehicleInsuranceCompany,
    VehicleAllocation
)

class VehicleAllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleAllocation
        fields = "__all__"
class VehicleInsuranceCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleInsuranceCompany
        fields = "__all__"
class VehicleDiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleDiary
        fields = "__all__"


class VehicleCompanyCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleCompanyCode
        fields = "__all__"


class VehicleBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleBasic
        fields = "__all__"


class VehicleSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleSummary
        fields = "__all__"


class VehicleInsuranceCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleInsuranceCompany
        fields = "__all__"


class VehicleTyreSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleTyre
        fields = "__all__"


class VehicleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleType
        fields = "__all__"


class VehicleStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleStatus
        fields = "__all__"


class VehicleReturnedWorkshopSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleReturnedWorkshop
        fields = "__all__"


class VehicleModelCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleModelCode
        fields = "__all__"


class VehicleMakeCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleMakeCode
        fields = "__all__"


class VehicleLocationCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleLocationCode
        fields = "__all__"


class VehicleInPullSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleInPull
        fields = "__all__"


class VehicleGearBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleGearBox
        fields = "__all__"


class VehicleFuelTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleFuelType
        fields = "__all__"


class VehicleDeductabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleDeductability
        fields = "__all__"


class VehicleCurrencyCodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleCurrencyCodes
        fields = "__all__"


class VehicleCountySerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleCounty
        fields = "__all__"


class VehicleCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleCountry
        fields = "__all__"


class VehicleCostCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleCostCenter
        fields = "__all__"


class VehicleConventionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleConventionType
        fields = "__all__"


class VehicleCompanyCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleCompanyCode
        fields = "__all__"


class VehicleBodyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleBodyType
        fields = "__all__"


class VehicleClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleClient
        fields = "__all__"


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = "__all__"
