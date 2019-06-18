from django.urls import path, include, re_path
from django.contrib import admin

urlpatterns = [
    re_path('admin/', admin.site.urls),
    path('tinymce/', include(('tinymce.urls'),)),
    path('', include(('gameregister.urls'),)),
]
