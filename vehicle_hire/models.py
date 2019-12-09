from django.db import models

# Create your models here.


class VehicleHireRentalRevenueInvoicedBy(models.Model):
    vehicle_rental_revenue_invoiced_by = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vehicle_rental_revenue_invoiced_by

class VehicleHireRentalPaymentStatus(models.Model):
    vehicle_rental_payment_status = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vehicle_rental_payment_status

class VehicleHireRentalPaymentRecievedBy(models.Model):
    vehicle_rental_payment_recieved_by = models.CharField(max_length=60)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vehicle_rental_revenue_invoiced_by
        
class VehicleHireRentalPaymentRecieved(models.Model):
    payment_recieved = models.FloatField(max_length=100)      

class VehicleHireRentalPaymentRecievedBy(models.Model):
    vehicle_rental_payment_recieved = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vehicle_rental_payment_recieved

class VehicleHireRentalInvoicesTo(models.Model):
    vehicle_rental_invoices_to = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vehicle_rental_invoices_to

class VehicleHireRentalDetailHiringDivision(models.Model):
    vehicle_rental_detail_hiring_division = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vehicle_rental_detail_hiring_division

class VehicleHireStatus(models.Model):
    vehicle_hire_status = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vehicle_hire_status

class VehicleHireRentalStatus(models.Model):
    vehicle_hire_rental_status = models.CharField(max_length=200)
    created_on =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vehicle_hire_rental_status

class VehicleHireReason(models.Model):
    vehicle_hire_reason = models.CharField(max_length=300)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vehicle_hire_reason

class VehicleHireCostCenter(models.Model):
    vehicle_hire_cost_center = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vehicle_hire_cost_center

class VehicleHire(models.Model):
    vehicle_hire_rental_code = models.CharField(max_length=60)
    vehicle_hire_registration_number = models.FloatField(max_length=60)
    vehicle_hire_extra_registration_number = models.FloatField(max_length=60)
    vehicle_hire_replaced_plate = models.FloatField(max_length=60)
    vehicle_hire_replaced_plate_cost_center = models.CharField(max_length=100)
    vehicle_hire_temprature_contract_end_date = models.DateField(auto_now_add=True)
    vehicle_hire_start_date = models.DateField(auto_now_add=True)
    vehicle_hire_end_date = models.DateField(auto_now_add=True)
    vehicle_hire_start_time = models.TimeField(auto_now_add=True)
    vehicle_hire_end_time = models.TimeField(auto_now_add=True)
    vehicle_hire_odometer_in = models.FloatField()
    vehicle_hire_odometer_out = models.FloatField()
    vehicle_hire_on_hire_reference = models.CharField(max_length=100)
    vehicle_hire_off_hire_reference = models.CharField(max_length=100)
    vehicle_hire_days = models.DateField(auto_now_add=True)
    vehicle_hire_distance = models.FloatField()
    vehicle_hire_comments = models.CharField(max_length=200)
    vehicle_hire_status = models.ForeignKey(VehicleHireStatus, on_delete=models.CASCADE)
    vehicle_hire_rental_status = models.ForeignKey(VehicleHireRentalStatus,on_delete=models.CASCADE)
    vehicle_hire_reason = models.ForeignKey(VehicleHireReason, on_delete=models.CASCADE)
    vehicle_hire_cost_center = models.ForeignKey(VehicleHireCostCenter, on_delete=models.CASCADE)

    def __str__(self):
        return self.vehicle_hire_rental_code

class VehicleHireRentalCollectionDetails(models.Model):
    name_of_the_person_collecting = models.CharField(max_length=60)
    collection_address = models.CharField(max_length=60)
    force_number = models.FloatField(max_length=40)
    telephone = models.IntegerField()
    hiring_division = models.ForeignKey(VehicleHireRentalDetailHiringDivision, on_delete=models.CASCADE)
    collection_post_code = models.CharField(max_length=30)
    created_on = models.DateTimeField(auto_now_add=True)
    vehicle_hire_id = models.ForeignKey(VehicleHire, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_of_the_person_collecting

class VehicleHireRentalRevenue(models.Model):
    payment_date = models.DateField(auto_now_add=True)
    payment_amount = models.FloatField()
    payment_recieved = models.ForeignKey(VehicleHireRentalPaymentRecieved, on_delete=models.CASCADE)
    vehicle_rental_invoices_to = models.ForeignKey(VehicleHireRentalInvoicesTo, on_delete=models.CASCADE)
    vehicle_rental_revenue_invoiced_by = models.ForeignKey(VehicleHireRentalRevenueInvoicedBy, on_delete=models.CASCADE)
    vehicle_rental_payment_status = models.ForeignKey(VehicleHireRentalPaymentStatus, on_delete=models.CASCADE)
    vehicle_rental_payment_recieved_by = models.ForeignKey(VehicleHireRentalPaymentRecievedBy, on_delete=models.CASCADE)  
    payment_details = models.CharField(max_length=100)
    date_assurance_authorized = models.DateField(auto_now_add=True)
    vehicle_insurance_days_off = models.DateField(auto_now_add=True)
    invoice_number = models.IntegerField()
    insurance_payment_days = models.DateField(auto_now_add=True)
    date_inv_prepared = models.DateField(auto_now_add=True)
    date_insurance_benefits_end = models.DateField(auto_now_add=True)
    daily_rental_charge = models.FloatField()
    invoice_date = models.DateField(auto_now_add=True)
    insurance_non_payment_days = models.DateField(auto_now_add=True)
    vehicle_hire_id = models.ForeignKey(VehicleHire, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.payment_details