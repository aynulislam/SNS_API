from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from visibility.models import SnVisibility


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_user')
    post_text = models.TextField(blank=True)
    post_date = models.DateTimeField(auto_now=True, blank=False)
    visibility_mode = models.ForeignKey('content.VisibilityMode', on_delete=models.CASCADE)
    visibility = GenericRelation(SnVisibility, related_query_name='post_visibility')

    def __str__(self):
        return self.post_text[0:10]
