# Generated by Django 3.0.4 on 2020-03-12 23:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0002_auto_20200311_2030'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Papers',
            new_name='Paper',
        ),
    ]
