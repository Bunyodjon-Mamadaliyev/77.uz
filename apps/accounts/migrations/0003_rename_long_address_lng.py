# Generated by Django 5.2 on 2025-07-10 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_alter_address_lat_alter_address_long"),
    ]

    operations = [
        migrations.RenameField(
            model_name="address",
            old_name="long",
            new_name="lng",
        ),
    ]
