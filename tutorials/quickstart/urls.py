from django.urls import path
from quickstart import views
from rest_framework.urlpatterns import format_suffix_patterns

# API endpoints
urlpatterns = format_suffix_patterns(
    [
        path("", views.api_root),
        path("quickstart/", views.SnippetList.as_view(), name="snippet-list"),
        path(
            "quickstart/<int:pk>/",
            views.SnippetDetail.as_view(),
            name="snippet-detail",
        ),
        path(
            "quickstart/<int:pk>/highlight/",
            views.SnippetHighlight.as_view(),
            name="snippet-highlight",
        ),
        path("users/", views.UserList.as_view(), name="user-list"),
        path(
            "users/<int:pk>/", views.UserDetail.as_view(), name="user-detail"
        ),
    ]
)

urlpatterns = format_suffix_patterns(urlpatterns)
