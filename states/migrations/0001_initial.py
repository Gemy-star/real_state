# Generated by Django 4.0.4 on 2022-05-08 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Country Name', max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Department Name', max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='states.country')),
            ],
        ),
        migrations.CreateModel(
            name='Developers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Department Name', max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(blank=True, max_length=255, null=True)),
                ('project_description', models.TextField(blank=True, null=True)),
                ('area', models.SmallIntegerField(blank=True, null=True)),
                ('min_price', models.SmallIntegerField(blank=True, null=True)),
                ('max_price', models.SmallIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50, verbose_name='status of state')),
                ('date_received', models.DateField(blank=True, null=True)),
                ('state_type', models.SmallIntegerField(blank=True, choices=[(1, 'فيلا'), (2, 'شقة'), (3, 'دوبلكس')], null=True)),
                ('area', models.IntegerField(blank=True, null=True)),
                ('max_price', models.SmallIntegerField(blank=True, null=True)),
                ('min_price', models.SmallIntegerField(blank=True, null=True)),
                ('rooms_number', models.SmallIntegerField(blank=True, null=True)),
                ('bathroom_number', models.SmallIntegerField(blank=True, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='states.department')),
            ],
        ),
        migrations.CreateModel(
            name='StateDeveloper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('developer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='states.developers')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='states.state')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectDevelopers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('developer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='states.developers')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='states.projects')),
            ],
        ),
    ]