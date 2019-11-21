from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('userApi/', include('user.urls')),
    path('snsApi/', include('sns.urls')),
    path('contentApi/', include('content.urls')),
    path('timelineApi/', include('timeline.urls')),
    path('shareApi/', include('share.urls')),
    path('rateApi/', include('rate.urls')),
    path('snviewsApi/', include('snview.urls')),
    path('activityApi/', include('activity.urls')),
    path('visibilityApi/', include('visibility.urls')),
    path('commentApi/', include('comment.urls')),
    path('generalApi/', include('general.urls')),
    path('reactApi/', include('react.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
