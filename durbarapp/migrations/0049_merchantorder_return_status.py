# Generated by Django 2.2 on 2022-01-03 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('durbarapp', '0048_auto_20220102_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='merchantorder',
            name='return_status',
            field=models.CharField(blank=True, choices=[('1', 'Customer_not_connected_phone'), ('2', 'Wrong_product'), ('3', 'Customer_abbsent_in_address'), ('4', 'Customer_not_interested_to_receve')], max_length=1),
        ),
    ]
