# Generated by Django 5.2.1 on 2025-05-21 04:53

import videoreciver.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videoreciver', '0002_mychunkedupload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dronevideo',
            name='file',
            field=models.FileField(upload_to=videoreciver.models.user_directory_path),
        ),
    ]
