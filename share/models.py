from django.db import models
from timeline.models import Post
from django.contrib.auth.models import User
from content.models import VisibilityMode
from django.contrib.contenttypes.fields import GenericRelation
from visibility.models import SnVisibility


# Create your models here.
class Share(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    share_text = models.TextField()
    vis_id = models.ForeignKey(VisibilityMode,on_delete=models.SET_NULL,null=True)
    visibility = GenericRelation(SnVisibility, related_query_name='share')

    def __str__(self):
        return self.user.username + " share " + self.post.post_text[:10]
