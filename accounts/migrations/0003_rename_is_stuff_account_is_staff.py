# Generated by Django 5.0.6 on 2024-06-12 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_account_phone_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='is_stuff',
            new_name='is_staff',
        ),
    ]
