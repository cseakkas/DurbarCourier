# Generated by Django 2.0.3 on 2021-12-13 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('durbarapp', '0014_auto_20211213_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchantorder',
            name='modify',
            field=models.DateTimeField(),
        ),
    ]
