# Generated by Django 3.0.4 on 2020-06-25 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0005_auto_20200312_2005'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paper',
            options={'ordering': ['-year']},
        ),
    ]
