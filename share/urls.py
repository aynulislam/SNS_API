from django.urls import path
from .views import ShareApiList
urlpatterns = [
    path('share_list/<pk>',ShareApiList.as_view(), name="share_list"),
    path('create_share/',ShareApiList.as_view(),name = 'create_share')
]
