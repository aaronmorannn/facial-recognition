from django.db import models

class UserProfile(models.Model):
    title = models.CharField(max_length=25, default='NULL USER')
    img = models.ImageField(upload_to="images/", default='null.jpg')


    def __str__(self):
        return self.title