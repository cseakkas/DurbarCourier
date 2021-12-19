# Generated by Django 2.0.3 on 2021-12-10 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('durbarapp', '0003_deliverycharge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliverycharge',
            name='delivery_charge_location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='durbarapp.DistrictEntry'),
        ),
        migrations.AlterField(
            model_name='deliverycharge',
            name='delivery_charge_weight',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='durbarapp.InsideOutsideLocation'),
        ),
    ]
