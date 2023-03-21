# Generated by Django 3.2.9 on 2023-03-20 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_name', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='ItemModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_code', models.CharField(blank=True, max_length=1024, unique=True)),
                ('description', models.CharField(max_length=1024)),
                ('location', models.CharField(max_length=1024)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('MRP', models.CharField(max_length=1024)),
                ('discount', models.CharField(max_length=1024)),
                ('mech_selling_pr', models.CharField(max_length=1024)),
                ('cust_selling_pr', models.CharField(max_length=1024)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('company_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company', to='store.companymodel')),
                ('vehicle_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicle', to='store.vehiclemodel')),
            ],
        ),
    ]
