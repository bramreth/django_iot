# Generated by Django 2.1.4 on 2018-12-05 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flood_monitoring_system', '0002_auto_20181205_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mqttwaterleveldata',
            name='id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
