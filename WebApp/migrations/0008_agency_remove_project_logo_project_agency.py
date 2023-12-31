# Generated by Django 4.2.4 on 2023-09-17 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0007_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='agency_logos/')),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='logo',
        ),
        migrations.AddField(
            model_name='project',
            name='agency',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='WebApp.agency'),
        ),
    ]
