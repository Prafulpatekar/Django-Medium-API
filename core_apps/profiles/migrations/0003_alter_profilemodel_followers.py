# Generated by Django 4.1.7 on 2024-06-22 19:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("profiles", "0002_rename_profile_profilemodel"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profilemodel",
            name="followers",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="following",
                to="profiles.profilemodel",
            ),
        ),
    ]
