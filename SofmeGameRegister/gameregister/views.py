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
from .forms import GameInfoForm, EditForm

def GameInfoView(request):
    form = GameInfoForm(request.POST or None, request.FILES)
    if request.method == "POST":
        ip, is_routable = get_client_ip(request)
        if form.is_valid():
            form.save()
            data = GameInfo.objects.get(pk = request.POST.get("game_id"))
            writeLog(request, data)
            return render(request, "gameregister/complete.html", {"title" : "ゲーム登録完了", "message" : data.game_uuid})
    else:
        form = GameInfoForm(initial = {
            "name": "", 
            "representative" : "", 
            "game_id" : "", 
            "discription" : "",
            "windows" : "",
            "android" : "",
            "vr" : "",
            "other" : "",
            "gamefile" : "",
            "panel" : "",
            "picture_1" : "",
            "picture_2" : "",
            "picture_3" : "",
            "movie" : "",
            })
    p = {
        "title" : "ゲーム情報登録",
        "form" : form,
        }
    return render(request, "gameregister/gameregisterform.html", p )

def complete(request):
    return render(request, "gameregister/complete.html")

def edit(request, editing_id):
    edit_form = EditForm()
    data = GameInfo.objects.get(pk = editing_id)
    form = GameInfoForm(request.POST, request.FILES, instance=data)
    uuid_error = ""
    message = ""

    if request.method == "POST":
        if request.POST.get("edit_uuid") == str(data.game_uuid) and form.is_valid():
            form.save()
            id = GameInfo.objects.get(pk = editing_id)
            writeLog(request, id)
            return render(request, "gameregister/complete.html", {"title" : "ゲーム更新完了", "message" : data})
        elif request.POST.get("edit_uuid") != str(data.game_uuid):
            uuid_error = "UUIDが異なります"
    else:
        form = GameInfoForm(initial = {
            "name": data.name, 
            "representative" : data.representative, 
            "game_id" : data.game_id, 
            "discription" : data.discription,
            "windows" : data.windows,
            "android" : data.android,
            "vr" : data.vr,
            "other" : data.other,
            "gamefile" : data.gamefile,
            "panel" : data.panel,
            "picture_1" : data.picture_1,
            "picture_2" : data.picture_2,
            "picture_3" : data.picture_3,
            "movie" : data.movie,
            })

    d = {
        "title": "登録情報更新",
        "message":message,
        "form":form,
        "edit_form": edit_form,
        "uuid_error":uuid_error,
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

def confirmation(request):
    d = {
        "title": "確認ページ",
        }
    return render(request, "gameregister/confirmation.html", d)