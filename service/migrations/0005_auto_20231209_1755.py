# Generated by Django 3.1.4 on 2023-12-09 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_auto_20231209_1718'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='fname',
            new_name='first_name',
        ),
    ]
