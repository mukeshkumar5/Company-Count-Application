# Generated by Django 5.1.1 on 2024-09-14 12:04

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("domain", models.CharField(blank=True, max_length=255, null=True)),
                ("year_founded", models.FloatField(blank=True, null=True)),
                ("industry", models.CharField(blank=True, max_length=255, null=True)),
                ("size_range", models.CharField(blank=True, max_length=100, null=True)),
                ("locality", models.CharField(blank=True, max_length=255, null=True)),
                ("country", models.CharField(blank=True, max_length=255, null=True)),
                ("linkedin_url", models.URLField(blank=True, null=True)),
                (
                    "current_employee_estimate",
                    models.IntegerField(blank=True, null=True),
                ),
                ("total_employee_estimate", models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
