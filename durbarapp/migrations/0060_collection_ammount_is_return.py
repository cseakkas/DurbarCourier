# Generated by Django 2.2 on 2022-01-07 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('durbarapp', '0059_auto_20220107_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection_ammount',
            name='is_return',
            field=models.BooleanField(default=False),
        ),
    ]
