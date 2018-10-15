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
from .logtype import LogType

from .models import GameInfo, Log
from .forms import GameInfoForm, EditForm, GameInfoFormEdit

BASE_URL = "/static/gameregister/file/"

def GameInfoView(request):
    form = GameInfoForm(request.POST or None, request.FILES)
    if request.method == "POST":
        ip, is_routable = get_client_ip(request)
        if form.is_valid():
            form.save()
            data = GameInfo.objects.get(pk = request.POST.get("game_id"))
            writeLog(request, data, LogType.NEW)
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
            "is_view":"",
            "is_mouse":"",
            "is_gamepad":"",
            "is_keyboard":"",
            "tag_list":"",
            })
    p = {
        "title" : "ゲーム情報登録",
        "form" : form,
        }
    writeLog(request, "" , LogType.ACCESS_REGISTER)
    return render(request, "gameregister/gameregisterform.html", p )

def complete(request):
    return render(request, "gameregister/complete.html")

def edit(request, editing_id):
    edit_form = EditForm()
    data = GameInfo.objects.get(pk = editing_id)
    form = GameInfoFormEdit(request.POST, request.FILES, instance=data)
    uuid_error = ""
    message = ""

    if request.method == "POST":
        if request.POST.get("edit_uuid") == str(data.game_uuid):
            if form.is_valid():
                form.save()
                id = GameInfo.objects.get(pk = editing_id)
                writeLog(request, id, LogType.UPDATE)

                return render(request, "gameregister/complete.html", {"title" : "ゲーム更新完了", "message" : data})
        elif request.POST.get("edit_uuid") != str(data.game_uuid):
            uuid_error = "UUIDが異なります"
            writeLog(request, "" , LogType.FAILED_UUID)
    else:
        form = GameInfoFormEdit(initial = {
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
            "is_view":data.is_view,
            "is_mouse":data.is_mouse,
            "is_gamepad":data.is_gamepad,
            "is_keyboard":data.is_keyboard,
            "tag_list":data.tag_list,
            })
    static_file = {
        "panel":data.panel,
        "picture_1":data.picture_1,
        "picture_2":data.picture_2,
        "picture_3":data.picture_3,
        "movie":data.movie,
        }
    d = {
        "title": "登録情報更新",
        "message":message,
        "form":form,
        "edit_form": edit_form,
        "uuid_error":uuid_error,
        "file":static_file,
    }
    writeLog(request, "" , LogType.ACCESS_EDIT)

    return render(request, "gameregister/edit.html", d)

def writeLog(request, id, type):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")

    if id == "":
        log = Log(ip = ip, access_type = LogType.string(type))
    else:
        log = Log(ip = ip, post = id, access_type = LogType.string(type))
    log.save()

def index(request):
    data = GameInfo.objects.all()
    d = {
        "title": "提出一覧",
        "data": data,
        }
    writeLog(request, "" , LogType.ACCESS_INDEX)
    return render(request, "gameregister/index.html", d)

def lp(request):
    d = {
        "title": "ランディングページ",
        }
    writeLog(request, "" , LogType.ACCESS_LP)
    return render(request, "gameregister/lp.html", d)

def confirmation(request):
    d = {
        "title": "確認ページ",
        }
    writeLog(request, "" , LogType.ACCESS_CONFIRMATION)
    return render(request, "gameregister/confirmation.html", d)

def admin_index(request):
    data = GameInfo.objects.all()
    d = {
        "title": "提出一覧",
        "data": data,
        }
    writeLog(request, "" , LogType.ACCESS_ADMIN_INDEX)
    return render(request, "gameregister/admin-index.html", d)