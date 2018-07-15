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
        return redirect("/complete")
    p = {
        "title" : "ゲーム情報登録",
        "form" : form,
        }
    return render(request, "gameregister/gameregisterform.html", p )

def complete(request):
    return render(request, "gameregister/complete.html")


def edit(request, editing_id):
    item = GameInfo.objects.get(pk = editing_id)
    if request.method == "POST":
        form = GameInfoForm(request.POST, request.FILES)
        if form.is_valid():
            GameInfo.objects.filter(pk=editing_id).update(value = form)
            return redirect("/complete")
    else:
        form = GameInfoForm()
    d = {
        "form": form,
    }
    d["form"] = GameInfo.objects.get(pk = editing_id)
    return render(request, "gameregister/edit.html", d)

def index(request):
    data = GameInfo.objects.all()
    d = {
        "title": "一覧",
        "data": data,
        }

    return render(request, 'gameregister/index.html', d)