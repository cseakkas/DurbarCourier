# Generated by Django 2.0.3 on 2021-12-11 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('durbarapp', '0009_auto_20211211_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchantorder',
            name='packegeType',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
