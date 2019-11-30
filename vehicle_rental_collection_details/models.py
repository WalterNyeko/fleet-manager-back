from django.db import models

# Create your models here.
class VehicleRentalCollectionDetails(models.Model):
    name_of_the_person_collecting = models.CharField(max_length=60)
    collection_address = models.CharField(max_length=60)
    force_number = models.FloatField(max_length=40)
    telephone = models.IntegerField()
    collection_post_code = models.CharField(max_length=30)
    created_on = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.name_of_the_person_collecting
