# Generated by Django 4.1.7 on 2023-02-28 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='NIP',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='patient',
            name='birth',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='patient',
            name='healthNo',
            field=models.CharField(max_length=20),
        ),
    ]