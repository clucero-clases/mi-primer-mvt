# Generated by Django 4.0.4 on 2022-05-19 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familia', '0004_domicilio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laboral',
            fields=[
                ('idPersona', models.BigIntegerField()),
                ('actividad', models.CharField(max_length=50)),
                ('antiguedad', models.IntegerField())
            ],
        ),
    ]
