# Generated by Django 4.2.4 on 2023-09-22 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0033_alter_image_foldername'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagefolder',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
