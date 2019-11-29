from django.urls import path, include
from rest_framework import routers
from .views import VehicleBodyTypeView

router = routers.DefaultRouter()
router.register(r'vehiclebodytypes', VehicleBodyTypeView)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
