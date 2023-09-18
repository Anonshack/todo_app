from django.shortcuts import render
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('users.urls')),
    path('todos/', include('app_todos.urls')),
    path('', include('pages.urls')),
]
