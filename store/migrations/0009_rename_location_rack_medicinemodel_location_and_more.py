# Generated by Django 4.1.5 on 2023-04-09 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_meddashboardmodel_medlocationmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicinemodel',
            old_name='location_rack',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='medlocationmodel',
            old_name='location_rack',
            new_name='location',
        ),
    ]
