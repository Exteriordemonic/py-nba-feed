from django.urls import include, path

from app.views import ApiHealthView

urlpatterns = [
    path("v1/health/", ApiHealthView.as_view(), name="api-v1-health"),
    path("users/", include("users.urls")),
    path("players/", include("players.urls")),
    path("teams/", include("teams.urls")),
    path("subscriptions/", include("subscriptions.urls")),
    path("feed/", include("feed.urls")),
]
