# Generated by Django 2.0.3 on 2021-12-11 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('durbarapp', '0007_auto_20211211_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchantorder',
            name='actual_package_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]