# Generated by Django 3.1.6 on 2021-02-15 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210215_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='location_name',
            field=models.CharField(max_length=50, verbose_name='название локации'),
        ),
    ]
