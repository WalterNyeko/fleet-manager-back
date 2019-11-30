# Generated by Django 2.2.7 on 2019-11-30 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0002_vehicleinsurancecompany'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='cost_per_km',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='cumilative_balance',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='estimated_odometer',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='l_per_km',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='next_inspection',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='next_service',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='number_of_remining_tyres',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='total_cost',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='vehicle_country',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='vehicle_currency_codes',
        ),
        migrations.CreateModel(
            name='VehicleSummary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estimated_odometer', models.CharField(max_length=250)),
                ('next_service', models.CharField(max_length=60)),
                ('next_inspection', models.CharField(max_length=60)),
                ('l_per_km', models.CharField(max_length=60)),
                ('cost_per_km', models.CharField(max_length=60)),
                ('total_cost', models.CharField(max_length=60)),
                ('number_of_remining_tyres', models.CharField(max_length=60)),
                ('cumilative_balance', models.CharField(max_length=60)),
                ('in_pull_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.VehicleInPull')),
                ('location_code_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.VehicleLocationCode')),
                ('vehicle_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.VehicleCountry')),
                ('vehicle_currency_codes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.VehicleCurrencyCodes')),
                ('vehicle_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.Vehicle')),
            ],
        ),
    ]