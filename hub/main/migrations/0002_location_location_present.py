# Generated by Django 3.1.6 on 2021-02-15 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='location_present',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
