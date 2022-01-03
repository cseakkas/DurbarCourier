# Generated by Django 2.2 on 2021-12-29 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('durbarapp', '0038_riderdeliveryorder_otp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection_ammount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipment_charge', models.CharField(blank=True, max_length=50)),
                ('cod_charge', models.CharField(blank=True, max_length=50)),
                ('lequed_or_Fragile_charge', models.CharField(blank=True, max_length=50)),
                ('total_service_charge', models.CharField(blank=True, max_length=50)),
                ('collection_amount', models.CharField(blank=True, max_length=50)),
                ('ordering', models.IntegerField(default=0)),
                ('modifed_by', models.IntegerField(default=0)),
                ('created_by', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modify', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=True)),
                ('rider_collection_time', models.DateTimeField(blank=True, null=True)),
                ('hub_collection_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('hub_statement_time', models.DateTimeField(blank=True, null=True)),
                ('head_ofice_collect_time', models.DateTimeField(blank=True, null=True)),
                ('merchant_statement_time', models.DateTimeField(blank=True, null=True)),
                ('merchant_collection_time', models.DateTimeField(blank=True, null=True)),
                ('collection_status', models.CharField(blank=True, choices=[('1', 'Rider'), ('2', 'Hub'), ('3', 'Head_Office'), ('4', 'Merchant')], default='1', max_length=1)),
                ('order_info', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='durbarapp.MerchantOrder')),
            ],
        ),
    ]