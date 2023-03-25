from django.contrib.auth.models import User
from django.db import models

class Userprofile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png')
    is_vendor = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
    