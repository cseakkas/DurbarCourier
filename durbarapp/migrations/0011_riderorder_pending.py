# Generated by Django 2.0.3 on 2021-12-12 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('durbarapp', '0010_auto_20211211_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='riderorder',
            name='pending',
            field=models.BooleanField(default=True),
        ),
    ]