# Generated by Django 4.0.4 on 2022-05-22 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('states', '0005_projects_department'),
        ('main', '0003_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='states.projects'),
        ),
    ]
