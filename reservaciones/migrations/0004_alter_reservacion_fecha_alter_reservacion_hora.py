# Generated by Django 5.0.1 on 2024-03-02 14:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservaciones', '0003_alter_destino_options_remove_reservacion_precio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservacion',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2024, 3, 2, 14, 17, 22, 310902, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='reservacion',
            name='hora',
            field=models.TimeField(default=datetime.datetime(2024, 3, 2, 14, 17, 22, 310902, tzinfo=datetime.timezone.utc)),
        ),
    ]
