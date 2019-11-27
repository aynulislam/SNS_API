from django.contrib import admin
from .models import (ShareReply,SnRatePost, SnRatePostComment, SnRateShareComment,
                     SnRatePostReplay, SnRateShareReplay, SnRateShare)
# Register your models here.

admin.site.register(SnRatePost)
admin.site.register(SnRatePostComment)
admin.site.register(SnRateShareComment)
admin.site.register(SnRatePostReplay)
admin.site.register(SnRateShareReplay)
admin.site.register(SnRateShare)
