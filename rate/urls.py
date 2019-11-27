from django.urls import path
from . import views

urlpatterns = [
   path('rate-post/<pk>', views.RatePostView.as_view(), name='rate-post'),
   path('rate-share/<pk>', views.RateShareView.as_view(), name='rate-share'),
   path('rate-post-comment/<pk>', views.RatePostCommentView.as_view(), name='rate-post-comment'),
   path('rate-post-replay/<pk>', views.RatePostReplayView.as_view(), name='rate-post-replay'),
   path('rate-share-comment/<pk>', views.RateShareCommentView.as_view(), name='rate-share-comment'),
   path('rate-share-replay/<pk>', views.RateShareReplayView.as_view(), name='rate-share-replay')
]
