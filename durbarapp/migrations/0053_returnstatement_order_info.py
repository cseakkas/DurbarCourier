# Generated by Django 2.2 on 2022-01-04 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('durbarapp', '0052_returnstatement'),
    ]

    operations = [
        migrations.AddField(
            model_name='returnstatement',
            name='order_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='durbarapp.MerchantOrder'),
        ),
    ]
