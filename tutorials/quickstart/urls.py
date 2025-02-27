"""This module defines the URL configuration for the quickstart app."""

from django.urls import include, path
from quickstart import views
from rest_framework.routers import DefaultRouter

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r"snippets", views.SnippetViewSet, basename="snippet")
router.register(r"users", views.UserViewSet, basename="user")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path("", include(router.urls)),
]

# This is the URL configuration file.
# Compare this snippet from tutorials/quickstart/views.py:
# """This module contains the view classes for quickstart app."""
