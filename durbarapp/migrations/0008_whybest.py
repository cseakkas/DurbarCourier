# Generated by Django 2.0.3 on 2021-09-13 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('durbarapp', '0007_auto_20210913_1928'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhyBest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cause', models.CharField(max_length=100)),
                ('icon', models.CharField(blank=True, max_length=50)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Why we are the best',
                'verbose_name_plural': 'Why we are the best',
            },
        ),
    ]