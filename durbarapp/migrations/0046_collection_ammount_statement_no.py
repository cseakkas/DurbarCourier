# Generated by Django 2.2 on 2022-01-01 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('durbarapp', '0045_auto_20211231_2318'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection_ammount',
            name='statement_no',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
