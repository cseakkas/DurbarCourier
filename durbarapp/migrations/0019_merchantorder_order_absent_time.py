# Generated by Django 2.0.3 on 2021-12-15 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('durbarapp', '0018_auto_20211215_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='merchantorder',
            name='order_absent_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
