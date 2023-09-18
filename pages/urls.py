from django.urls import path

from .views import HomePageView, UsersListView

urlpatterns = [
    path('users/', UsersListView.as_view(), name='users'),
    path('', HomePageView.as_view(), name='home'),
]