# Generated by Django 4.1.2 on 2022-11-07 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0011_alter_settings_clientlogo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='clientLogo',
            field=models.ImageField(default='default_logo.jpg', upload_to='company_logos'),
        ),
    ]
