# Generated by Django 2.2 on 2022-01-06 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('durbarapp', '0055_auto_20220104_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='riderdeliveryorder',
            name='return_product_delevery',
            field=models.BooleanField(default=False),
        ),
    ]
