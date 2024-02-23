# Generated by Django 5.0.2 on 2024-02-21 13:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0004_alter_booking_destination_remove_source_city_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='destination',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='destination', to='testapp.airport'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='source',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='source', to='testapp.airport'),
        ),
    ]
