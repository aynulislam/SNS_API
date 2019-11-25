from django.contrib import admin
from .models import SnAction, GnOnlineStatus, SnActionType
# Register your models here.

admin.site.register(SnAction)
admin.site.register(GnOnlineStatus)
admin.site.register(SnActionType)
