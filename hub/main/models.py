from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    location_name = models.CharField('название локации', max_length=50)
    location_present = models.CharField('описание локации', max_length=500, blank=True, null=True)

    def __str__(self):
        return self.location_name





class RegistrationLocation(models.Model):
    reg_id = models.AutoField(primary_key=True)
    location = models.ManyToManyField(Location)
    course_name = models.CharField('тема мероприятия', max_length=100)
    course_org = models.CharField('организатор мероприятия', max_length=100)
    inform = models.TextField('информация', max_length=400)
    email = models.EmailField('почта организатора', max_length=100)
    many_course = models.IntegerField('количество человек')
    created = models.DateTimeField(default=timezone.now)


class Comentary(models.Model):
    location = models.ManyToManyField(Location)
    id = models.AutoField(primary_key=True)
    comentary = models.TextField('Коментарий', max_length=200)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    created = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.comentary},{self.location}'
