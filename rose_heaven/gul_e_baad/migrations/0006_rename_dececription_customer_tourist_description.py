# Generated by Django 4.1.3 on 2022-11-15 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("gul_e_baad", "0005_alter_adeemaform_1_datetime"),
    ]

    operations = [
        migrations.RenameField(
            model_name="customer_tourist",
            old_name="dececription",
            new_name="description",
        ),
    ]
