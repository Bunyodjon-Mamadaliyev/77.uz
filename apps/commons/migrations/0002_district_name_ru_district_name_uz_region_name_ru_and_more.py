# Generated by Django 5.2 on 2025-07-17 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("commons", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="district",
            name="name_ru",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="district",
            name="name_uz",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="region",
            name="name_ru",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="region",
            name="name_uz",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
