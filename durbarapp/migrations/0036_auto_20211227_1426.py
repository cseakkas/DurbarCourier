# Generated by Django 2.2 on 2021-12-27 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('durbarapp', '0035_auto_20211226_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riderdeliveryorder',
            name='order_status',
            field=models.CharField(blank=True, choices=[('1', 'Collect'), ('2', 'Delivered'), ('3', 'collection_submit_to_hub'), ('4', 'return'), ('5', 'return_to_hub')], default='1', max_length=1),
        ),
    ]
