# Generated by Django 4.0.4 on 2022-05-22 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_contact_sent_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('mini_description', models.TextField(blank=True, null=True)),
                ('full_description', models.TextField(blank=True, null=True)),
                ('more_description', models.TextField(blank=True, null=True)),
                ('background', models.ImageField(blank=True, null=True, upload_to='blogs-images/')),
            ],
        ),
    ]
