from django.urls import path, include
from rest_framework import routers
from .views import VehicleTyreView

router = routers.DefaultRouter()
router.register(r'vehicletyres', VehicleTyreView)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
