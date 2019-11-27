from django.urls import path
from .views import PostApi, PostDetails, PostList
urlpatterns = [
    path('post/', PostApi.as_view(), name="post"),
    path('post_details/<pk>', PostDetails.as_view(), name="post"),
    path('postlists/', PostList.as_view(), name='test')
]
