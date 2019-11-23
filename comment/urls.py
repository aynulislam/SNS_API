from django.urls import path
from .views import PostCommentApiView, PostReplyApiView, ShareCommentApiView, ShareReplyApiView

urlpatterns = [
    path('post-comment/<pk>', PostCommentApiView.as_view(), name="post_comment"),
    path('post-reply/<pk>', PostReplyApiView.as_view(), name="post_replay"),
    path('share-comment/<pk>', ShareCommentApiView.as_view(), name="share_comment"),
    path('share-replay/<pk>', ShareReplyApiView.as_view(), name="share_reply")
]
