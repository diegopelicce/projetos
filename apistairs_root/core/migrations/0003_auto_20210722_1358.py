# Generated by Django 3.2.5 on 2021-07-22 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210722_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horariodisponivel',
            name='data',
            field=models.DateField(default=''),
        ),
        migrations.AlterField(
            model_name='horariodisponivel',
            name='horario',
            field=models.TimeField(default='', max_length=50),
        ),
    ]