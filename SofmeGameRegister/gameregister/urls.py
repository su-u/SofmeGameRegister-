from django.conf.urls import url
from gameregister import views



urlpatterns = [
    url("^register$", views.GameInfoView, name = "GameInfoView"),
    url(r"^complete", views.complete, name = "complete"),
    url(r"^edit/(?P<editing_id>\d+)/$", views.edit, name="edit"),
    url(r"^index$", views.index, name="index"),
    url(r"^$", views.lp, name = "lp"),
]