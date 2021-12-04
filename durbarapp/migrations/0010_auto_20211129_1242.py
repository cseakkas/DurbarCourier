# Generated by Django 2.0.3 on 2021-11-29 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('durbarapp', '0009_hubinfo_riderinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hubinfo',
            name='contact_no1',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='hubinfo',
            name='email',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
    ]
