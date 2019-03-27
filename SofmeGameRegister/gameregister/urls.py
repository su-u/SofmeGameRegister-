from django.conf.urls import url
from gameregister import views
from django.contrib import admin


urlpatterns = [
    url("^register$", views.GameInfoView, name = "GameInfoView"),
    url(r"^complete", views.complete, name = "complete"),
    url(r"^edit/(?P<editing_id>\d+)/$", views.edit, name="edit"),
    url(r"^index$", views.index, name="index"),
    url(r"^$", views.lp, name = "Lp"),
    url(r"^confirmation$", views.confirmation, name = "Confirmation"),
    url(r"^adminindex$", views.admin_index, name = "Admin-index"),
    url(r"^manual$", views.manual_page, name = "Manual-Page"),
    url(r"^movie$", views.movie_page, name = "Movie-Page"),

    url(r"^body$", views.body, name = "body"),
]

