# Generated by Django 4.1.3 on 2022-11-15 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gul_e_baad", "0004_alter_adeemaform_1_datetime"),
    ]

    operations = [
        migrations.AlterField(
            model_name="adeemaform_1",
            name="datetime",
            field=models.CharField(default="", max_length=50),
        ),
    ]
