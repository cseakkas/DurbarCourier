# Generated by Django 2.0.3 on 2021-12-15 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('durbarapp', '0022_auto_20211215_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riderinfo',
            name='modify',
            field=models.DateTimeField(),
        ),
    ]
