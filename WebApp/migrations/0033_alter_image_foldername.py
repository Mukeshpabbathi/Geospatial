# Generated by Django 4.2.4 on 2023-09-22 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0032_imagefolder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='foldername',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='WebApp.imagefolder'),
        ),
    ]
