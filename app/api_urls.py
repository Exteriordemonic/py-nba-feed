from django.urls import path

from app.views import ApiHealthView

urlpatterns = [
    path("v1/health/", ApiHealthView.as_view(), name="api-v1-health"),
]
