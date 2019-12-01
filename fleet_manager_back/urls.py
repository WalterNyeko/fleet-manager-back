
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from vehicle.views import VehicleView
from vehicle_hire.views import VehicleHireView,VehicleHireRentalRevenueView,VehicleHireRentalRevenueInvoicedByView,VehicleHireRentalPaymentRecievedByView,VehicleHireCostCenterView, VehicleHireReasonView,VehicleHireRentalStatusView, VehicleHireStatusView, VehicleHireRentalCollectionDetailsView,VehicleHireRentalDetailHiringDivisionView,VehicleHireRentalInvoicesToView, VehicleHireRentalPaymentRecievedView,VehicleHireRentalPaymentStatusView


# Serializers define the API representation.


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff'],


# ViewSets define the view behavior.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'vehicles', VehicleView)
router.register(r'vehiclehire',VehicleHireView)
router.register(r'vehiclehirecostcenter',VehicleHireCostCenterView)
router.register(r'vehicle_hire_reason', VehicleHireReasonView)
router.register(r'vehicle_hire_rental_status', VehicleHireRentalStatusView)
router.register(r'vehicle_hire_status', VehicleHireStatusView)
router.register(r'vehicle_hire_rental_collection_details', VehicleHireRentalCollectionDetailsView)
router.register(r'vehicle_hire_rental_detail_hiring_division', VehicleHireRentalCollectionDetailsView)
router.register(r'vehicle_hire_rental_invoices_to', VehicleHireRentalInvoicesToView)
router.register(r'vehicle_hire_rental_payment_recieved', VehicleHireRentalPaymentRecievedView)
router.register(r'vehicle_hire_rental_payment_recieved_by', VehicleHireRentalPaymentRecievedByView)
router.register(r'vehicle_hire_rental_payment_status', VehicleHireRentalPaymentStatusView)
router.register(r'vehicle_hire_rental_revenue_invoiced_by', VehicleHireRentalRevenueInvoicedByView)
router.register(r'vehicle_rental_revenue',VehicleHireRentalRevenueView)
router.register(r'vehicle_hire_rental_collection_details', VehicleHireRentalCollectionDetailsView)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^admin/', admin.site.urls),    
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace="home"))
]
