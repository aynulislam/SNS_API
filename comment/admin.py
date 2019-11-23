from django.contrib import admin
from .models import \
    PostComment, PostReply, ShareComment, ShareReply, \
    PostCommentContent, PostReplyContent, ShareCommentContent, ShareReplyContent

# Register your models here.
my_models = [PostComment, PostReply, ShareComment, ShareReply,
             PostCommentContent, PostReplyContent, ShareCommentContent, ShareReplyContent]
admin.site.register(my_models)
