from django.db import models
from django.contrib.auth.models import User
from timeline.models import Post
from share.models import Share


class SnPostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    view_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username + " visited " + self.post.post_text[0:10]


class SnShareView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    share = models.ForeignKey(Share, on_delete=models.CASCADE)
    view_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username + " visited " + self.share.post.post_text[0:10]
