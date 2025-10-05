from django.contrib import admin
from django.urls import path, include
import fitapp.profile.urls as profile_urls
from django.views.generic import TemplateView


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path("admin/", admin.site.urls),
    path("profile/", include(profile_urls)),
    path("sentry-debug/", trigger_error),
    path("", TemplateView.as_view(template_name="profile/success.html"), name="home"),
]
