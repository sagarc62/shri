# Generated by Django 5.0.2 on 2024-02-21 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_airport_destination_city_source_city_booking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='Destination',
            new_name='destination',
        ),
    ]