# Generated by Django 4.0.8 on 2022-11-30 02:03

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("route_planner", "0003_route"),
    ]

    operations = [
        migrations.AlterField(
            model_name="route",
            name="route_points",
            field=django.contrib.gis.db.models.fields.LineStringField(srid=4326),
        ),
    ]
