from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^tinymce/', include('tinymce.urls')),
    url(r"", include("gameregister.urls")),
    url(r"^admin/", include(admin.site.urls)),
]
