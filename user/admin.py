from django.contrib import admin
from .models import ScUser,ScLoginHistory

# Register your models here.

admin.site.register(ScUser)
admin.site.register(ScLoginHistory)
