from django.db import models
from django.contrib.auth.models import User
from timeline.models import Post
from share.models import Share
from comment.models import PostComment, PostReply, ShareComment, ShareReply
from general.models import SnAction


class SnReactPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='react_post')
    react_type = models.ForeignKey(SnAction, on_delete=models.SET_NULL, null=True)
    react_post_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.react_type.action_name


class SnReactPostComment:
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(PostComment, on_delete=models.CASCADE)
    react_type = models.ForeignKey(SnAction, on_delete=models.CASCADE)
    react_date = models.DateTimeField(auto_now=True)


class SnReactPostReply:
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reply = models.ForeignKey(PostReply, on_delete=models.CASCADE)
    react_type = models.ForeignKey(SnAction, on_delete=models.CASCADE)
    react_date = models.DateTimeField(auto_now=True)


class SnReactShareComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(ShareComment, on_delete=models.CASCADE)
    react_type = models.ForeignKey(SnAction, on_delete=models.CASCADE)
    react_date = models.DateTimeField(auto_now=True)


class SnReactShareReply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reply = models.ForeignKey(ShareReply, on_delete=models.CASCADE)
    react_type = models.ForeignKey(SnAction, on_delete=models.CASCADE)
    react_date = models.DateTimeField(auto_now=True)


class SnReactShare(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    share = models.ForeignKey(Share, on_delete=models.CASCADE, related_name='shared_post')
    react_type = models.ForeignKey(SnAction, on_delete=models.SET_NULL, null=True, related_name='reacted_type')
    react_post_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
