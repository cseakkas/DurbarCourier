# Generated by Django 2.0.3 on 2021-09-12 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('durbarapp', '0004_courierprofile_districtentry_hubinfo_merchantinfo_postofficeinfo_sliderinfo_upazillaentry'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollectionPointEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_point_name_bangla', models.CharField(max_length=230)),
                ('collection_point_name_english', models.CharField(max_length=230)),
                ('ordering', models.IntegerField(default=0)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='MerchantOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=50)),
                ('customer_id', models.CharField(max_length=50)),
                ('customer_name', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('contact_no1', models.CharField(max_length=50)),
                ('contact_no2', models.CharField(max_length=50)),
                ('reference_no', models.CharField(max_length=50)),
                ('actual_package_price', models.IntegerField(default=0)),
                ('collection_date', models.DateTimeField()),
                ('collection_time_morning', models.BooleanField(default=False)),
                ('collection_time_evening', models.BooleanField(default=False)),
                ('only_delivery', models.BooleanField(default=False)),
                ('delivery_and_amount_collection', models.BooleanField(default=False)),
                ('lequed_or_Fragile', models.BooleanField(default=False)),
                ('weight', models.FloatField(default=0)),
                ('addtional_note', models.TextField()),
                ('service_charge', models.CharField(max_length=50)),
                ('ordering', models.IntegerField(default=0)),
                ('modifed_by', models.IntegerField(default=0)),
                ('created_by', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modify', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=True)),
                ('collection_point', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='durbarapp.CollectionPointEntry')),
                ('district_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='durbarapp.DistrictEntry')),
                ('upazilla_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='durbarapp.UpazillaEntry')),
            ],
        ),
        migrations.CreateModel(
            name='UnionEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('union_name_bangla', models.CharField(max_length=230)),
                ('union_name_english', models.CharField(max_length=230)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=1)),
                ('upazilla_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='durbarapp.UpazillaEntry')),
            ],
        ),
    ]