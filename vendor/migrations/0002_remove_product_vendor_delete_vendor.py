# Generated by Django 5.0.2 on 2024-04-12 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='vendor',
        ),
        migrations.DeleteModel(
            name='Vendor',
        ),
    ]
