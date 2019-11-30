from rest_framework import serializers
from .models import VehicleRentalCollectionDetails

class VehicleRentalCollectionDetailsSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleRentalCollectionDetails
        fields = ('name_of_the_person_collecting','collection_address','force_number','telephone','collection_post_code', 'created_on')
