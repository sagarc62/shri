# Generated by Django 5.0.2 on 2024-02-21 13:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_rename_destination_booking_destination'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='destination',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='destination', to='testapp.city'),
        ),
        migrations.RemoveField(
            model_name='source_city',
            name='name',
        ),
        migrations.AlterField(
            model_name='booking',
            name='source',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='source', to='testapp.city'),
        ),
        migrations.DeleteModel(
            name='Destination_city',
        ),
        migrations.DeleteModel(
            name='Source_city',
        ),
    ]