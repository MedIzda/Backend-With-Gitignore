# Generated by Django 4.1.7 on 2023-03-02 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0003_remove_patient_nip_remove_patient_added_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clinic',
            name='NIP',
        ),
        migrations.RemoveField(
            model_name='clinic',
            name='REGON',
        ),
        migrations.RemoveField(
            model_name='clinic',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='clinic',
            name='phoneNo',
        ),
    ]
