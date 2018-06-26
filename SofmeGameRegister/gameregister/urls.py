from django.conf.urls import url
from gameregister import views



urlpatterns = [
    url("^$", views.GameInfoView, name = "GameInfoView"),
    url(r"^complete", views.complete, name = "complete"),
]