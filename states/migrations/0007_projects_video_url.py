# Generated by Django 4.0.4 on 2022-05-22 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('states', '0006_projects_background_1_projects_background_2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='video_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]