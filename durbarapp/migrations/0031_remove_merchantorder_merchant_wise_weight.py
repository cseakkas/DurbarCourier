# Generated by Django 2.2 on 2021-12-22 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('durbarapp', '0030_merchantorder_merchant_wise_weight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='merchantorder',
            name='merchant_wise_weight',
        ),
    ]
