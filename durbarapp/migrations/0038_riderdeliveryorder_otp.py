# Generated by Django 2.2 on 2021-12-28 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('durbarapp', '0037_riderdeliveryorder_return_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='riderdeliveryorder',
            name='otp',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]