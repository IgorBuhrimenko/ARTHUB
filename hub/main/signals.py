from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import Comentary


@receiver(post_save, sender=Comentary)
def add_coments(sender, instance, **kwargs):
    if instance is True:
        print("okey, Post save ")
    else:
        print('Rabotaet')


@receiver(pre_save,sender=Comentary)
def pre_save(sender, instance, **kwargs):
    if instance is True:
        print("okey, Post save ")
    else:
        print('Rabotaet')

