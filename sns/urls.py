from django.urls import path
from . import views

urlpatterns = [
    path('friendrequest/', views.SnGiveFriendRequest.as_view(), name='registration'),
    path('delete/<pk>', views.DeleteRequest.as_view(), name="delete_request"),
    path('accept/<pk>', views.AcceptRequest.as_view(), name="accept_request"),
    path('skip/<pk>', views.SkipRequest.as_view(), name="skip_request"),
    path('unblock/<pk>', views.UnBlock.as_view(), name="delete_request"),
    path('unfriend/<pk>', views.UnFriend.as_view(), name="unfriend"),
    path('unfollow/<pk>', views.UnFollow.as_view(), name="unfollow"),
    path('follow/', views.SnFollowView.as_view(), name="follow"),
    path('block/<pk>', views.BlockFriend.as_view(), name="block"),
]
