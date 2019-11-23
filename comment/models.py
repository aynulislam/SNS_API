from django.db import models
from timeline.models import Post
from content.models import SnContentType
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from visibility.models import SnVisibility


# Comment table for each original post
class PostComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_body = models.TextField()
    comment_date = models.DateTimeField(auto_now=True)
    voice = models.FileField(blank=True, null=True)
    visibility_mode = models.ForeignKey('content.VisibilityMode', on_delete=models.SET_NULL, null=True)
    visibility = GenericRelation(SnVisibility, related_query_name='post_comment')

    def __str__(self):
        return self.comment_body[0:10]


# Content table for each PostComment
class PostCommentContent(models.Model):
    content_type = models.ForeignKey(SnContentType, on_delete=models.CASCADE)
    content = models.FileField(blank=True, null=True)
    comment = models.ForeignKey(PostComment, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.content)


# Replay table for each reply for a original post
class PostReply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(PostComment, on_delete=models.CASCADE)
    comment_body = models.TextField()
    comment_date = models.DateTimeField(auto_now=True)
    voice = models.FileField(blank=True)
    visibility_mode = models.ForeignKey('content.VisibilityMode', on_delete=models.SET_NULL, null=True)
    visibility = GenericRelation(SnVisibility, related_query_name='post_reply')

    def __str__(self):
        return self.comment_body[0:10]


# Content table for each PostReply
class PostReplyContent(models.Model):
    content_type = models.ForeignKey(SnContentType, on_delete=models.CASCADE)
    content = models.FileField(blank=True, null=True)
    replay = models.ForeignKey(PostReply, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.content)


# Comment table for each shared post
class ShareComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    share = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_body = models.TextField()
    comment_date = models.DateTimeField(auto_now=True)
    voice = models.FileField(blank=True)
    visibility_mode = models.ForeignKey('content.VisibilityMode', on_delete=models.SET_NULL, null=True)
    visibility = GenericRelation(SnVisibility, related_query_name='share_comment')

    def __str__(self):
        return self.comment_body[0:10]


# Content table for each ShareComment
class ShareCommentContent(models.Model):
    content_type = models.ForeignKey(SnContentType, on_delete=models.CASCADE)
    content = models.FileField(blank=True, null=True)
    comment = models.ForeignKey(ShareComment, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.content)


# Replay table for each comment for a shared post
class ShareReply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(ShareComment, on_delete=models.CASCADE)
    comment_body = models.TextField()
    comment_date = models.DateTimeField(auto_now=True)
    voice = models.FileField(blank=True)
    visibility_mode = models.ForeignKey('content.VisibilityMode', on_delete=models.SET_NULL, null=True)
    visibility = GenericRelation(SnVisibility, related_query_name='share_reply')

    def __str__(self):
        return self.comment_body[0:10]


# Content table for each ShareReply
class ShareReplyContent(models.Model):
    content_type = models.ForeignKey(SnContentType, on_delete=models.CASCADE)
    content = models.FileField(blank=True, null=True)
    replay = models.ForeignKey(ShareReply, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.content)
