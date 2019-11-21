from django.urls import path
from .views import ActivityListView
urlpatterns = [
    path('activity-list/', ActivityListView.as_view(), name='activity_list')
]
