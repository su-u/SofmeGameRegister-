from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)
from django.http import HttpResponse
from django import forms
from django.template.context_processors import csrf
from django.views.generic import CreateView, UpdateView
import logging

from .models import GameInfo
from .forms import GameInfoForm


def GameInfoView(request):
    form = GameInfoForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        data = GameInfo.objects.get(pk = request.POST["game_id"])
        return render(request, "gameregister/complete.html", {"title" : "ゲーム登録完了", "message" : data.game_uuid})
    p = {
        "title" : "ゲーム情報登録",
        "form" : form,
        }
    return render(request, "gameregister/gameregisterform.html", p )

def complete(request):
    return render(request, "gameregister/complete.html")


def edit(request, editing_id):
    data = GameInfo.objects.get(pk = editing_id)
    if request.method == "POST":
        form = GameInfoForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            #GameInfo.objects.filter(pk=editing_id).update(value = form)
            form.save()
            return render(request, "gameregister/complete.html", {"title" : "ゲーム更新完了", "message" : data})
            #return redirect("/complete",{"title" : "ゲーム更新完了", "message" : "a"})
    else:
        form = GameInfoForm(initial = {
            "name": data.name, 
            "representative" : data.representative, 
            "game_id" : data.game_id, 
            "discription" : data.discription, 
            "gamefile" : data.gamefile,
            "panel" : data.panel,
            "picture_1" : data.picture_1,
            "picture_2" : data.picture_2,
            "picture_3" : data.picture_3,
            "movie" : data.movie
            })
    d = {
        "title": "登録情報更新",
        "form": form,
    }
    return render(request, "gameregister/gameregisterform.html", d)

def index(request):
    data = GameInfo.objects.all()
    d = {
        "title": "提出一覧",
        "data": data,
        }

    return render(request, 'gameregister/index.html', d)