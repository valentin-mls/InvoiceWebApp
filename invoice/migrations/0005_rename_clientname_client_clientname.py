# Generated by Django 4.1.2 on 2022-11-04 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0004_rename_nom_client_clientname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='ClientName',
            new_name='clientName',
        ),
    ]