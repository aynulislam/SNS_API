from django.contrib import admin
from .models import SnReactPost,SnReactShare, SnReactPostComment, \
    SnReactPostReply, SnReactShareComment, SnReactShareReply

# Register your models here.

admin.site.register(SnReactPost)
admin.site.register(SnReactShare)
