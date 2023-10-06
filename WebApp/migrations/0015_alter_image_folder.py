# Generated by Django 4.2.4 on 2023-09-21 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0014_folder_image_folder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='folder',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='WebApp.folder'),
        ),
    ]
