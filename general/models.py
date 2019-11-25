from django.db import models


class SnActionType(models.Model):
    action_name = models.CharField(max_length=20)

    def __str__(self):
        return self.action_name


class SnAction(models.Model):
    action_name = models.CharField(max_length=20)
    action_type = models.ForeignKey(SnActionType, on_delete=models.SET_NULL, null=True, related_name='action_type_name')

    def __str__(self):
        return self.action_name


class GnOnlineStatus(models.Model):
    online_status = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.online_status
