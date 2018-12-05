# Generated by Django 2.1.4 on 2018-12-05 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flood_monitoring_system', '0004_auto_20181205_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='mqttwaterleveldata',
            name='time',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mqttwaterleveldata',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterUniqueTogether(
            name='mqttwaterleveldata',
            unique_together={('id', 'hardware_serial')},
        ),
    ]
