# Generated by Django 4.1.2 on 2022-11-07 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0007_invoice_product_alter_product_invoice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='product',
        ),
    ]