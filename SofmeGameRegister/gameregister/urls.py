from django.urls import path, include, re_path
from gameregister import views
from django.contrib import admin


urlpatterns = [
    path("register", views.GameInfoView, name = "GameInfoView"),
    path("complete", views.complete, name = "complete"),
    path("edit/<int:editing_id>/", views.edit, name="edit"),
    path("index", views.index, name="index"),
    path("", views.lp, name = "Lp"),
    path("confirmation", views.confirmation, name = "Confirmation"),
    path("adminindex", views.admin_index, name = "Admin-index"),
    path("manual", views.manual_page, name = "Manual-Page"),
    path("movie", views.movie_page, name = "Movie-Page"),
    path("signbord",views.sign_bord_page, name = "Sign-Bord-Page"),

    path("body", views.body, name = "body"),
]

