from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfile(models.Model):
    
    # Sets up models for user accounts
    #
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to='images', default="null.jpg", blank=True)
    # description = models.CharField(max_length=100, default="default")

    # Error cant seem to fix 
    # NOT NULL constraint failed: accounts_userprofile.description


def __str__(self): 
        return self.user 
    
def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)

