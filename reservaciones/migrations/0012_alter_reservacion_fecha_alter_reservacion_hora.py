# Generated by Django 5.0.1 on 2024-03-31 22:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservaciones', '0011_alter_reservacion_fecha_alter_reservacion_hora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservacion',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2024, 3, 31, 22, 54, 54, 154842, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='reservacion',
            name='hora',
            field=models.TimeField(default=datetime.datetime(2024, 3, 31, 22, 54, 54, 154842, tzinfo=datetime.timezone.utc)),
        ),
    ]