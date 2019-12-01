from rest_framework import viewsets
from .models import (
    VehicleInsuranceCompany,
    Vehicle,
    VehicleClient,
    VehicleBodyType,
    VehicleConventionType,
    VehicleCostCenter,
    VehicleCompanyCode,
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
    VehicleSummary,
    VehicleBasic,
    VehicleDiary,
    VehicleInsuranceCompany,
    VehicleAllocation,
    VehicleAssets,
    VehicleNotes,
    VehicleRepair,
    RepairSupply,
    RepairDescription,
    RepairWorkshop,
    RepairReason,
    RepairJobStatus,
    RepairPaperworkStatus,
    RepairEstimationCost,
    RepairInvoiceDetails,
    RepairInvoicedTo,
    RepairRecievedBy,
)
from .serializers import (
    VehicleInsuranceCompanySerializer,
    VehicleSerializer,
    VehicleClientSerializer,
    VehicleBodyTypeSerializer,
    VehicleCompanyCodeSerializer,
    VehicleConventionTypeSerializer,
    VehicleCostCenterSerializer,
    VehicleCountrySerializer,
    VehicleCountySerializer,
    VehicleCurrencyCodesSerializer,
    VehicleDeductabilitySerializer,
    VehicleFuelTypeSerializer,
    VehicleGearBoxSerializer,
    VehicleInPullSerializer,
    VehicleLocationCodeSerializer,
    VehicleMakeCodeSerializer,
    VehicleModelCodeSerializer,
    VehicleReturnedWorkshopSerializer,
    VehicleStatusSerializer,
    VehicleTypeSerializer,
    VehicleTyreSerializer,
    VehicleSummarySerializer,
    VehicleBasicSerializer,
    VehicleDiarySerializer,
    VehicleInsuranceCompanySerializer,
    VehicleAllocationSerializer,
    VehicleAssetsSerializer,
    VehicleNotesSerializer,
    VehicleRepairSerializer,
    RepairSupplySerializer,
    RepairDescriptionSerializer,
    RepairWorkshopSerializer,
    RepairReasonSerializer,
    RepairJobStatusSerializer,
    RepairPaperworkStatusSerializer,
    RepairEstimationCostSerializer,
    RepairInvoiceDetailsSerializer,
    RepairInvoicedToSerializer,
    RepairRecievedBySerializer,
)
from rest_framework.permissions import IsAuthenticated


class RepairRecievedByView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = RepairRecievedBy.objects.all()
    serializer_class = RepairRecievedBySerializer


class RepairInvoiceDetailsView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = RepairInvoiceDetails.objects.all()
    serializer_class = RepairInvoiceDetailsSerializer


class RepairEstimationCostView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = RepairEstimationCost.objects.all()
    serializer_class = RepairEstimationCostSerializer


class RepairPaperworkStatusView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = RepairPaperworkStatus.objects.all()
    serializer_class = RepairPaperworkStatusSerializer


class RepairJobStatusView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = RepairJobStatus.objects.all()
    serializer_class = RepairJobStatusSerializer


class RepairReasonView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = RepairReason.objects.all()
    serializer_class = RepairReasonSerializer


class RepairWorkshopView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = RepairWorkshop.objects.all()
    serializer_class = RepairWorkshopSerializer


class RepairDescriptionView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = RepairDescription.objects.all()
    serializer_class = RepairDescriptionSerializer


class RepairSupplyView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = RepairSupply.objects.all()
    serializer_class = RepairSupplySerializer


class VehicleRepairView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleRepair.objects.all()
    serializer_class = VehicleRepairSerializer


class VehicleNotesView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleNotes.objects.all()
    serializer_class = VehicleNotesSerializer


class VehicleAssetsView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleAssets.objects.all()
    serializer_class = VehicleAssetsSerializer


class VehicleAllocationView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleAllocation.objects.all()
    serializer_class = VehicleAllocationSerializer


class VehicleInsuranceCompanyView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleInsuranceCompany.objects.all()
    serializer_class = VehicleInsuranceCompanySerializer


class VehicleBasicView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleBasic.objects.all()
    serializer_class = VehicleBasicSerializer


class VehicleDiaryView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleDiary.objects.all()
    serializer_class = VehicleDiarySerializer


class VehicleSummaryView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleSummary.objects.all()
    serializer_class = VehicleSummarySerializer


class VehicleInsuranceCompanyView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleInsuranceCompany.objects.all()
    serializer_class = VehicleInsuranceCompanySerializer


class VehicleTyreView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleTyre.objects.all()
    serializer_class = VehicleTyreSerializer


class VehicleTypeView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer


class VehicleStatusView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleStatus.objects.all()
    serializer_class = VehicleStatusSerializer


class VehicleReturnedWorkshopView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleReturnedWorkshop.objects.all()
    serializer_class = VehicleReturnedWorkshopSerializer


class VehicleModelCodeView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleModelCode.objects.all()
    serializer_class = VehicleModelCodeSerializer


class VehicleMakeCodeView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleMakeCode.objects.all()
    serializer_class = VehicleMakeCodeSerializer


class VehicleLocationCodeView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleLocationCode.objects.all()
    serializer_class = VehicleLocationCodeSerializer


class VehicleInPullView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleInPull.objects.all()
    serializer_class = VehicleInPullSerializer


class VehicleGearBoxView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleGearBox.objects.all()
    serializer_class = VehicleGearBoxSerializer


class VehicleFuelTypeView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleFuelType.objects.all()
    serializer_class = VehicleFuelTypeSerializer


class VehicleDeductabilityView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleDeductability.objects.all()
    serializer_class = VehicleDeductabilitySerializer


class VehicleCurrencyCodesView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleCurrencyCodes.objects.all()
    serializer_class = VehicleCurrencyCodesSerializer


class VehicleCountyView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleCounty.objects.all()
    serializer_class = VehicleCountySerializer


class VehicleCountryView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleCountry.objects.all()
    serializer_class = VehicleCountrySerializer


class VehicleCostCenterView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleCostCenter.objects.all()
    serializer_class = VehicleCostCenterSerializer


class VehicleConventionTypeView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleConventionType.objects.all()
    serializer_class = VehicleConventionTypeSerializer


class VehicleCompanyCodeView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleCompanyCode.objects.all()
    serializer_class = VehicleCompanyCodeSerializer


class VehicleBodyTypeView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleBodyType.objects.all()
    serializer_class = VehicleBodyTypeSerializer


class VehicleClientView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleClient.objects.all()
    serializer_class = VehicleClientSerializer


class VehicleView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
