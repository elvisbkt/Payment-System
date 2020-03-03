from django.db import models
from django.contrib.auth.models import Group
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.db.models.signals import post_save, pre_save

class User(AbstractUser):
    username = models.CharField(blank=True, null=True, max_length=255)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

def add_to_default_group(sender, instance, **kwargs):
    user = instance
    if kwargs["created"]:
        group = Group.objects.get(name='Worker')
        user.groups.add(group)


post_save.connect(add_to_default_group, sender=User)

def default():
    default_dict = {"key": "value"}
    return default_dict


class UserProfile(models.Model):
    user = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)
    firstname = models.CharField(max_length=50, blank=True)
    lastname = models.CharField(max_length=50, blank=True)
    dateofbirth = models.CharField(max_length=255, blank=True)
    phonenumber = models.IntegerField(max_length=25, blank=True,null=True)
    IDnumber = models.IntegerField(blank=True,null=True)
    gender = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return '{}'.format(self.user)
    
    objects = models.Manager()


def create_dummy_profile(sender, instance, ** kwargs):
    user_id = instance.id
    if kwargs["created"]:
        profile = UserProfile.objects.create(user=instance)
        profile.save()


post_save.connect(create_dummy_profile, sender=User)
