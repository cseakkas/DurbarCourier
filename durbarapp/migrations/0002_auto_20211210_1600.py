# Generated by Django 2.0.3 on 2021-12-10 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('durbarapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deliverycharge',
            name='delivery_charge_location',
        ),
        migrations.RemoveField(
            model_name='deliverycharge',
            name='delivery_charge_weight',
        ),
        migrations.DeleteModel(
            name='DeliveryCharge',
        ),
    ]
