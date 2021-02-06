"""base URL Configuration"""
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.urls import include, path
from userManage import urls


urlpatterns = [path("admin/", admin.site.urls), path("", include(urls))]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
