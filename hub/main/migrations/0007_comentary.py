# Generated by Django 3.1.6 on 2021-02-19 13:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210215_2332'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentary',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('comentary', models.TextField(max_length=200, verbose_name='Коментарий')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('active', models.BooleanField(default=True)),
                ('location', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.location')),
            ],
        ),
    ]
