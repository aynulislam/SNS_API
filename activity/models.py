from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# Create your models here.


class SnActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    entity_id = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    value_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('entity_id', 'content_object')

    def __str__(self):
        return self.user.username
