# Generated by Django 3.1.6 on 2021-02-15 13:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_location_location_present'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationLocation',
            fields=[
                ('reg_id', models.AutoField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=100)),
                ('course_org', models.CharField(max_length=100)),
                ('inform', models.TextField(max_length=400)),
                ('email', models.EmailField(max_length=100)),
                ('many_course', models.IntegerField()),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('location', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.location')),
            ],
        ),
    ]
