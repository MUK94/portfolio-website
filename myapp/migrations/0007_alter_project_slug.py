# Generated by Django 4.0.5 on 2022-11-19 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_project_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(max_length=255, unique_for_date='publish'),
        ),
    ]
