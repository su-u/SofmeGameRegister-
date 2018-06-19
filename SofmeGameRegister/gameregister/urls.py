from django.conf.urls import url
from gameregister import views

urlpatterns = [
    url('^$', views.kakikomi, name='kakikomi'),
]