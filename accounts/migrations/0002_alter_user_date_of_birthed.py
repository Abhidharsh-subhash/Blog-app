# Generated by Django 4.2.5 on 2023-09-27 07:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="date_of_birthed",
            field=models.DateField(null=True),
        ),
    ]
