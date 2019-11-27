from django.contrib import admin
from .models import SnRequest,SnFriend,SnBlock,SnFollow
# Register your models here.


admin.site.register(SnRequest)
admin.site.register(SnFriend)
admin.site.register(SnFollow)
admin.site.register(SnBlock)
