# Generated by Django 5.0.2 on 2024-03-05 05:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0004_alter_userprofile_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="username",
            field=models.CharField(max_length=100),
        ),
    ]
