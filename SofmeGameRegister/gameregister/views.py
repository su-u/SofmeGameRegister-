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
from ipware import get_client_ip

from .models import GameInfo, Log
from .forms import GameInfoForm

def GameInfoView(request):
    form = GameInfoForm(request.POST or None, request.FILES)
    if request.method == "POST":
        ip, is_routable = get_client_ip(request)
        if form.is_valid():
            form.save()
            data = GameInfo.objects.get(pk = request.POST["game_id"])
            writeLog(request, data)
            return render(request, "gameregister/complete.html", {"title" : "ゲーム登録完了", "message" : data.game_uuid})
    else:
        form = GameInfoForm(initial = {
            "name": "", 
            "representative" : "", 
            "game_id" : "", 
            "discription" : "", 
            "gamefile" : "",
            "panel" : "",
            "picture_1" : "",
            "picture_2" : "",
            "picture_3" : "",
            "movie" : "",
            "edit_id":"",
            })
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
            form.save()
            id = GameInfo.objects.get(pk = editing_id)
            writeLog(request, id)
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
        "form":form,
    }
    return render(request, "gameregister/edit.html", d)

def writeLog(request, id):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    log = Log(ip = ip, post = id)
    log.save()

def index(request):
    data = GameInfo.objects.all()
    d = {
        "title": "提出一覧",
        "data": data,
        }

    return render(request, "gameregister/index.html", d)

def lp(request):
    d = {
        "title": "ランディングページ",
        }
    return render(request, "gameregister/lp.html", d)

