# Generated by Django 4.1 on 2024-03-20 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("checkout", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="discount", name="discount_value", field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name="price", name="price", field=models.FloatField(),
        ),
    ]