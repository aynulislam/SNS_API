from django.contrib import admin
from .models import SnAlbumType, SnContentType, VisibilityMode, SnContentDetail,SnAlbum
# Register your models here.

admin.site.register(SnAlbumType)
admin.site.register(SnContentType)
admin.site.register(VisibilityMode)
admin.site.register(SnContentDetail)
admin.site.register(SnAlbum)
