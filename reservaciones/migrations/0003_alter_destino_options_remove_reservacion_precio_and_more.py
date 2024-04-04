# Generated by Django 5.0.1 on 2024-03-02 14:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservaciones', '0002_origen'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='destino',
            options={'verbose_name': 'Destino', 'verbose_name_plural': 'Destinos'},
        ),
        migrations.RemoveField(
            model_name='reservacion',
            name='precio',
        ),
        migrations.AddField(
            model_name='reservacion',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2024, 3, 2, 14, 16, 17, 433027, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='reservacion',
            name='hora',
            field=models.TimeField(default=datetime.datetime(2024, 3, 2, 14, 16, 17, 433027, tzinfo=datetime.timezone.utc)),
        ),
    ]