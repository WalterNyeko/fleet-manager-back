from django.db import models


class VehicleInsuranceCompany(models.Model):
    insurance_company_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tyre_name


class VehicleTyre(models.Model):
    tyre_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tyre_name


class VehicleType(models.Model):
    type_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type_name


class VehicleStatus(models.Model):
    status_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status_name


class VehicleReturnedWorkshop(models.Model):
    returned_workshop_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.returned_workshop_name


class VehicleModelCode(models.Model):
    model_code_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.model_code_name


class VehicleMakeCode(models.Model):
    make_code_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.make_code_name


class VehicleLocationCode(models.Model):
    location_code_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.location_code_name


class VehicleInPull(models.Model):
    in_pull_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.in_pull_name


class VehicleGearBox(models.Model):
    gear_box_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.gear_box_name


class VehicleFuelType(models.Model):
    fuel_type_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fuel_type_name


class VehicleDeductability(models.Model):
    deductability_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.deductability_name


class VehicleCurrencyCodes(models.Model):
    currency_codes_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.currency_codes_name


class VehicleCounty(models.Model):
    county_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.county_name


class VehicleCountry(models.Model):
    country_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.country_name


class VehicleCostCenter(models.Model):
    cost_center_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cost_center_name


class VehicleConventionType(models.Model):
    convention_type_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.convention_type_name


class VehicleCompanyCode(models.Model):
    company_code_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_code_name


class VehicleBodyType(models.Model):
    body_type_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body_type_name


class VehicleClient(models.Model):
    client_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.client_name


class Vehicle(models.Model):
    registration_no = models.CharField(max_length=60)
    extra_registration_no = models.CharField(max_length=60)
    year = models.CharField(max_length=60)
    fleet_number = models.CharField(max_length=60)
    date_registered = models.DateTimeField(auto_now_add=True)
    date_returned_to_workshop = models.DateTimeField(auto_now_add=True)
    vehicle_tyre = models.ForeignKey(VehicleTyre, on_delete=models.CASCADE)
    vehicle_body_type = models.ForeignKey(VehicleBodyType, on_delete=models.CASCADE)
    vehicle_client = models.ForeignKey(VehicleClient, on_delete=models.CASCADE)
    vehicle_company_code = models.ForeignKey(
        VehicleCompanyCode, on_delete=models.CASCADE
    )
    vehicle_convention_type = models.ForeignKey(
        VehicleConventionType, on_delete=models.CASCADE
    )
    vehicle_cost_center = models.ForeignKey(VehicleCostCenter, on_delete=models.CASCADE)
    vehicle_fuel_type = models.ForeignKey(VehicleFuelType, on_delete=models.CASCADE)
    vehicle_make_code = models.ForeignKey(VehicleMakeCode, on_delete=models.CASCADE)
    vehicle_model_code = models.ForeignKey(VehicleModelCode, on_delete=models.CASCADE)
    vehicle_returned_workshop = models.ForeignKey(
        VehicleReturnedWorkshop, on_delete=models.CASCADE
    )
    vehicle_status = models.ForeignKey(VehicleStatus, on_delete=models.CASCADE)
    vehicle_county = models.ForeignKey(VehicleCounty, on_delete=models.CASCADE)
    vehicle_location_code = models.ForeignKey(
        VehicleLocationCode, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.registration_no


class VehicleSummary(models.Model):
    estimated_odometer = models.CharField(max_length=250)
    location_code_name = models.ForeignKey(
        VehicleLocationCode, on_delete=models.CASCADE
    )
    vehicle_country = models.ForeignKey(VehicleCountry, on_delete=models.CASCADE)
    next_service = models.CharField(max_length=60)
    next_inspection = models.CharField(max_length=60)
    vehicle_currency_codes = models.ForeignKey(
        VehicleCurrencyCodes, on_delete=models.CASCADE
    )
    in_pull_name = models.ForeignKey(VehicleInPull, on_delete=models.CASCADE)
    l_per_km = models.CharField(max_length=60)
    cost_per_km = models.CharField(max_length=60)
    total_cost = models.CharField(max_length=60)
    number_of_remining_tyres = models.CharField(max_length=60)
    cumilative_balance = models.CharField(max_length=60)
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)


class VehicleBasic(models.Model):
    exterior_color = models.CharField(max_length=60)
    vehicle_gear_box = models.ForeignKey(VehicleGearBox, on_delete=models.CASCADE)
    ecoscore = models.CharField(max_length=60)
    interior_color = models.CharField(max_length=60)
    number_of_doors = models.CharField(max_length=60)
    co2km = models.CharField(max_length=60)
    key_number = models.CharField(max_length=60)
    chassis_number = models.CharField(max_length=60)
    fiscal_hp = models.CharField(max_length=60)
    engiene_number = models.CharField(max_length=60)
    engiene_cc = models.CharField(max_length=60)
    distance_to_work = models.CharField(max_length=60)
    vehicle_phone_number = models.CharField(max_length=60)
    bhp = models.CharField(max_length=60)
    vehicle_deductability = models.ForeignKey(
        VehicleDeductability, on_delete=models.CASCADE
    )
    gross_vehicle_weight = models.CharField(max_length=60)
    winter_tyres = models.CharField(max_length=60)
    winter_tyres_location = models.CharField(max_length=60)
    tank_size = models.CharField(max_length=60)
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)


class VehicleDiary(models.Model):
    waranty = models.CharField(max_length=60)
    waranty_distance = models.CharField(max_length=60)
    vehicle_insurance_company = models.ForeignKey(
        VehicleInsuranceCompany, on_delete=models.CASCADE
    )
    insurance_expiry = models.CharField(max_length=60)
    insurance_commencement = models.CharField(max_length=60)
    insurance_certificate = models.CharField(max_length=60)
    motor_insurance_policy_no = models.CharField(max_length=60)
    mid_on = models.CharField(max_length=60)
    mid_off = models.CharField(max_length=60)
    insurance_certificate = models.CharField(max_length=60)
    service_date = models.CharField(max_length=60)
    last_service_type = models.CharField(max_length=60)
    service_schedule = models.CharField(max_length=60)
    service_interval_weeks = models.CharField(max_length=60)
    service_interval_kms = models.CharField(max_length=60)
    inspection_date = models.CharField(max_length=60)
    inspection_type = models.CharField(max_length=60)
    inspection_interval_weeks = models.CharField(max_length=60)
    inspection_interval_distance = models.CharField(max_length=60)
    inspection_certificate_no = models.CharField(max_length=60)
    distance_per_year = models.CharField(max_length=60)
    distance_per_day = models.CharField(max_length=60)
    age_years = models.CharField(max_length=60)
    age_days = models.CharField(max_length=60)
    deviation = models.CharField(max_length=60)
    deviation_perc = models.CharField(max_length=60)
    odometer = models.CharField(max_length=60)
    current_odo_date = models.CharField(max_length=60)
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    # accidents / repairs here

class VehicleAllocation(models.Model):
    driver_name = models.CharField(max_length=60)
    registratyion_no = models.CharField(max_length=60)
    changed_by = models.CharField(max_length=60)
    date = models.CharField(max_length=60)
    company_code = models.CharField(max_length=60)
    cost_center = models.CharField(max_length=60)
    start_date = models.CharField(max_length=60)
    odometer = models.CharField(max_length=60)
    end_date = models.CharField(max_length=60)
    end_odometer = models.CharField(max_length=60)
    lock = models.CharField(max_length=60)
    workshop = models.CharField(max_length=60)
    allocation_reason = models.CharField(max_length=60)
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

class VehicleAssets(models.Model):
    registration_no = models.CharField(max_length=60)
    extra_registration_no = models.CharField(max_length=60)
    asset_description = models.CharField(max_length=60)
    asset_type = models.CharField(max_length=60)
    asset_make = models.CharField(max_length=60)
    asset_model = models.CharField(max_length=60)
    asset_issue_date = models.CharField(max_length=60)
    asset_return_date = models.CharField(max_length=60)
    asset_serial = models.CharField(max_length=60)
    driver_name = models.CharField(max_length=60)
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

