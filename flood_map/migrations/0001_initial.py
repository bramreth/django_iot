# Generated by Django 2.1.3 on 2018-12-04 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='environmental_agency_flood_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor_id', models.CharField(max_length=80)),
                ('label', models.CharField(max_length=40)),
                ('town', models.CharField(max_length=40)),
                ('river', models.CharField(max_length=40)),
                ('lat', models.DecimalField(decimal_places=7, max_digits=9)),
                ('long', models.DecimalField(decimal_places=7, max_digits=10)),
                ('reading', models.FloatField()),
                ('time', models.DateTimeField()),
            ],
        ),
    ]
