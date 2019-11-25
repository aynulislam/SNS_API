from django.urls import path
from .views import ActionView, SearchView

urlpatterns = [
    path('action-list/', ActionView.as_view(), name="action-list"),
    path('search/<key>',SearchView.as_view(), name='search')
]
