# Generated by Django 2.2 on 2022-01-02 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('durbarapp', '0046_collection_ammount_statement_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection_ammount',
            name='collection_status',
            field=models.CharField(blank=True, choices=[('1', 'Rider'), ('2', 'Hub'), ('3', 'Receve_Pending_Head_Office'), ('4', 'Head_Office'), ('5', 'Merchant')], default='1', max_length=1),
        ),
    ]