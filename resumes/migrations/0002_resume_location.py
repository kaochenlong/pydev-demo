# Generated by Django 5.1.3 on 2024-11-25 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("resumes", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="resume",
            name="location",
            field=models.CharField(max_length=200, null=True),
        ),
    ]
