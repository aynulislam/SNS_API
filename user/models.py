from django.db import models
from django.contrib.auth.models import User
from general.models import GnOnlineStatus
# Create your models here.


class ScUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    user_code = models.CharField(max_length=10, unique=True)
    user_name = models.CharField(max_length=100, blank=False)
    phone = models.CharField(max_length=100, blank=True)
    voice = models.FileField(blank=True)
    face = models.FileField(blank=True)
    pin = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user_name


class ScLoginHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mac_address = models.CharField(max_length=20, blank=True)
    ip = models.GenericIPAddressField(blank=True, null=True)
    in_time = models.DateTimeField(auto_now=True, blank=False)
    out_time = models.DateTimeField(auto_now=False, blank=True, null=True)
    online_status = models.ForeignKey(GnOnlineStatus, null=True, on_delete=models.SET_NULL, blank=False, default=False)

    def __str__(self):
        return self.user.username

