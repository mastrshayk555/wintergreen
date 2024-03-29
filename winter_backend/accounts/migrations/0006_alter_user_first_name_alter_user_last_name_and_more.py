# Generated by Django 5.0.1 on 2024-01-20 14:00

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0005_alter_useraddress_address_two"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="phone",
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True, max_length=128, null=True, region=None
            ),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="date_of_birth",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="financial_goals",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="industry",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="job_title",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="life_goals",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="marital_status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("single", "Single"),
                    ("married", "Married"),
                    ("widowed", "Widowed"),
                    ("divorced", "Divorced"),
                    ("other", "Other"),
                ],
                max_length=50,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="number_of_children",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="salary",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
