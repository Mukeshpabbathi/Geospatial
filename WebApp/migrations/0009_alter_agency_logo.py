# Generated by Django 4.2.4 on 2023-09-17 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0008_agency_remove_project_logo_project_agency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agency',
            name='logo',
            field=models.FileField(upload_to='agency_logos/'),
        ),
    ]
