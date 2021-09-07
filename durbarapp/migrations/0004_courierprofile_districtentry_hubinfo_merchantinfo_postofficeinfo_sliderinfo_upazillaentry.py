# Generated by Django 2.2.1 on 2021-09-07 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('durbarapp', '0003_delete_custom'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourierProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courier_name', models.CharField(blank=True, max_length=100)),
                ('slugan', models.CharField(blank=True, max_length=100)),
                ('page_title', models.CharField(blank=True, max_length=100)),
                ('email1', models.EmailField(blank=True, max_length=100)),
                ('email2', models.EmailField(blank=True, max_length=100)),
                ('mobile1', models.CharField(blank=True, max_length=15)),
                ('mobile2', models.CharField(blank=True, max_length=15)),
                ('address', models.TextField(blank=True)),
                ('pro_details', models.TextField(blank=True)),
                ('logo', models.ImageField(upload_to='images/logo')),
                ('favicon_logo', models.ImageField(upload_to='images/logo')),
                ('about_content', models.TextField(blank=True)),
                ('about_images', models.ImageField(upload_to='images/about_images')),
                ('why_buy', models.TextField(blank=True)),
                ('map_locationo', models.TextField(blank=True)),
                ('facebook_link', models.TextField(blank=True)),
                ('instagram_link', models.TextField(blank=True)),
                ('youtube_link', models.TextField(blank=True)),
                ('linkedin_link', models.TextField(blank=True)),
                ('staring_year', models.IntegerField()),
                ('copy_right', models.CharField(blank=True, max_length=50)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'courier Profile',
                'verbose_name_plural': 'courier Profile Information',
            },
        ),
        migrations.CreateModel(
            name='DistrictEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name_bangla', models.CharField(max_length=230)),
                ('district_name_english', models.CharField(max_length=230)),
                ('ordering', models.IntegerField(default=0)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='SliderInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider_name', models.CharField(blank=True, max_length=100)),
                ('title1', models.CharField(blank=True, max_length=200)),
                ('title2', models.CharField(blank=True, max_length=200)),
                ('slider_images', models.ImageField(upload_to='images/slider')),
                ('slider_link', models.TextField(blank=True)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('slider_order', models.IntegerField()),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Slider Image',
                'verbose_name_plural': 'Slider Images',
            },
        ),
        migrations.CreateModel(
            name='UpazillaEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upazilla_name_bangla', models.CharField(max_length=230)),
                ('upazilla_name_english', models.CharField(max_length=230)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=1)),
                ('district_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='durbarapp.DistrictEntry')),
            ],
        ),
        migrations.CreateModel(
            name='PostOfficeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_office_bangla', models.CharField(max_length=230)),
                ('post_office_english', models.CharField(max_length=230)),
                ('post_code', models.CharField(max_length=230)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=1)),
                ('upazilla_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='durbarapp.UpazillaEntry')),
            ],
        ),
        migrations.CreateModel(
            name='MerchantInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marchant_name', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('contact_no1', models.CharField(max_length=50)),
                ('contact_no2', models.CharField(max_length=50)),
                ('logo', models.ImageField(upload_to='images/merchant_logo')),
                ('ordering', models.IntegerField(default=0)),
                ('modifed_by', models.IntegerField(default=0)),
                ('created_by', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modify', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=True)),
                ('district_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='durbarapp.DistrictEntry')),
                ('upazilla_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='durbarapp.UpazillaEntry')),
            ],
        ),
        migrations.CreateModel(
            name='HubInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hub_name_bangla', models.CharField(max_length=230)),
                ('Hub_name_english', models.CharField(max_length=230)),
                ('address', models.TextField()),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('contact_no1', models.CharField(max_length=50)),
                ('contact_no2', models.CharField(max_length=50)),
                ('ordering', models.IntegerField(default=0)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('district_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='durbarapp.DistrictEntry')),
                ('upazilla_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='durbarapp.UpazillaEntry')),
            ],
        ),
    ]