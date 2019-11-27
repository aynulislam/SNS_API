from django.urls import path
from .views import VisibilityListView
urlpatterns = [
    path('visibility-list/', VisibilityListView.as_view(), name='visibility_list')
]
