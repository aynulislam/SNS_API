from django.urls import path
from .views import PostVisitView, ShareVisitView
urlpatterns = [
    path('post-visit/<pk>', PostVisitView.as_view(), name='post-visit'),
    path('share-visit/<pk>', ShareVisitView.as_view(), name='share-visit')
]
