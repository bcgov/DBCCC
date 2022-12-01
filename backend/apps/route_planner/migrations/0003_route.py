# Generated by Django 4.0.8 on 2022-11-29 21:52

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("route_planner", "0002_alter_traveladvisorymessage_options_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Route",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("email", models.EmailField(max_length=254)),
                (
                    "start_point",
                    django.contrib.gis.db.models.fields.PointField(srid=4326),
                ),
                (
                    "destination_point",
                    django.contrib.gis.db.models.fields.PointField(srid=4326),
                ),
                (
                    "route_points",
                    django.contrib.gis.db.models.fields.MultiPointField(srid=4326),
                ),
                (
                    "criteria",
                    models.CharField(
                        choices=[("fastest", "Fastest"), ("shortest", "Shortest")],
                        default="fastest",
                        max_length=10,
                    ),
                ),
                ("srs_code", models.CharField(max_length=5)),
                (
                    "distance_unit",
                    models.CharField(
                        choices=[("km", "km"), ("mi", "mi")], default="km", max_length=2
                    ),
                ),
                (
                    "distance",
                    models.FloatField(help_text="Length of route in distance units"),
                ),
                ("route_time", models.FloatField(help_text="Duration in seconds")),
            ],
            options={
                "abstract": False,
            },
        ),
    ]