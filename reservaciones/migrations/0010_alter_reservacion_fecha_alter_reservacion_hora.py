# Generated by Django 5.0.1 on 2024-03-08 01:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservaciones', '0009_reservacion_a_nombre_de_alter_reservacion_fecha_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservacion',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2024, 3, 8, 1, 43, 25, 824960, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='reservacion',
            name='hora',
            field=models.TimeField(default=datetime.datetime(2024, 3, 8, 1, 43, 25, 824960, tzinfo=datetime.timezone.utc)),
        ),
    ]