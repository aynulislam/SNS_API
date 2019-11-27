from django.urls import path
from .views import PostReactApiList, ShareReactApiList

urlpatterns = [
    path('post-react/<pk>', PostReactApiList.as_view(), name="post_reacts"),
    path('share_reacts/<pk>', ShareReactApiList.as_view(), name='share_reacts')
]
