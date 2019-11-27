from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class SnRequest(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    user_id_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="request_to")
    request_date = models.DateTimeField(blank=False, auto_now=True)

    def __str__(self):
        return self.user_id.username+" to "+self.user_id_to.username


class SnFriend(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    user_id_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="friend_to")
    friend_date = models.DateTimeField(blank=False, auto_now=True)

    def __str__(self):
        return self.user_id.username+" to "+self.user_id_to.username


class SnFollow(models.Model):
    follow_id = models.ForeignKey(User, on_delete=models.CASCADE)
    user_id_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follow_to")
    follow_date = models.DateTimeField(blank=False, auto_now=True)

    def __str__(self):
        return self.follow_id.username+" to "+self.user_id_to.username


class SnBlock(models.Model):
    block_id = models.ForeignKey(User, on_delete=models.CASCADE)
    user_id_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="block_to")
    block_date = models.DateTimeField(blank=False, auto_now=True)

    def __str__(self):
        return self.block_id.username+" to "+self.user_id_to.username
