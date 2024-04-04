# Generated by Django 5.0.1 on 2024-03-31 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='fecha_annadido',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='auto',
            name='km_recorridos',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='auto',
            name='Imagen',
            field=models.ImageField(upload_to='media/img/'),
        ),
    ]
