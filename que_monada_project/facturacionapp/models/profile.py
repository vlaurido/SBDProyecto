from django.db import models
from django.contrib.auth.models import User
from .role import Role

class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, related_name='profile', on_delete=models.CASCADE)
    role = models.ForeignKey(Role, null=False, blank=False, on_delete=models.DO_NOTHING)

    def __unicode__(self):
        return self.user.username

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
