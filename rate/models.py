from django.db import models
from django.contrib.auth.models import User
from general.models import SnAction
from timeline.models import Post
from share.models import Share
from comment.models import PostComment, PostReply, ShareComment, ShareReply
# Create your models here.


class SnRatePost(models.Model):
    class Meta:
        unique_together = (('user', 'post'),)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    rate = models.PositiveSmallIntegerField(range(0, 5), default=0)
    rate_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username + ": " + str(self.rate)


class SnRateShare(models.Model):
    class Meta:
        unique_together = (('user', 'share'),)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    share = models.ForeignKey(Share, on_delete=models.CASCADE)
    rate = models.PositiveSmallIntegerField(range(0, 5), default=0)
    rate_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username + ": " + str(self.rate)


class SnRatePostComment(models.Model):
    class Meta:
        unique_together = (('user', 'comment'),)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(PostComment, on_delete=models.CASCADE)
    rate = models.PositiveSmallIntegerField(range(0, 5), default=0)
    rate_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username + ": " + str(self.rate)


class SnRatePostReplay(models.Model):
    class Meta:
        unique_together = (('user', 'post_replay'),)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_replay = models.ForeignKey(PostReply, on_delete=models.CASCADE)
    rate = models.PositiveSmallIntegerField(range(0, 5), default=0)
    rate_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username + ": " + str(self.rate)


class SnRateShareComment(models.Model):
    class Meta:
        unique_together = (('user', 'share_comment'),)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    share_comment = models.ForeignKey(ShareComment, on_delete=models.CASCADE)
    rate = models.PositiveSmallIntegerField(range(0, 5), default=0)
    rate_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username + ": " + str(self.rate)


class SnRateShareReplay(models.Model):
    class Meta:
        unique_together = (('user', 'share_replay'),)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    share_replay = models.ForeignKey(ShareReply, on_delete=models.CASCADE)
    rate = models.PositiveSmallIntegerField(range(0, 5), default=0)
    rate_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username+": "+str(self.rate)
