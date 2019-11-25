from django.urls import path, include
from .views import (AlbumListView, AlbumDetailView, ContentView,
                    ContentTypeView, VisibilityListView, PostContent)

urlpatterns = [
    path('album_list/', AlbumListView.as_view(), name="album_list"),
    path('album/<pk>', AlbumDetailView.as_view(), name="album_detail"),
    path('content/<pk>', ContentView.as_view(), name="content"),
    path('visibility/', VisibilityListView.as_view(), name="content"),
    path('content-type/', ContentTypeView.as_view(), name='content-type'),
    path('post_list/', PostContent.as_view(), name='post-content')
]
