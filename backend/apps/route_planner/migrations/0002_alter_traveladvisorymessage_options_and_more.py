# Generated by Django 4.0.8 on 2022-11-29 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("route_planner", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="traveladvisorymessage",
            options={"verbose_name": "Travel Advisory Message"},
        ),
        migrations.AddField(
            model_name="traveladvisorymessage",
            name="title",
            field=models.CharField(default="", max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="traveladvisorymessage",
            name="pub_date",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Publication date"
            ),
        ),
    ]
