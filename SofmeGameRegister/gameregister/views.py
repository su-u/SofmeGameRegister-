from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.views.generic import CreateView, UpdateView
import logging

from .models import GameInfo
from .forms import GameInfoForm


def GameInfoView(request):
    form = GameInfoForm(request.POST or None, request.FILES)
    if 'button_1' in request.POST:
        # ボタン1がクリックされた場合の処理
        form.fields['aname'] = forms.CharField(label='すいま')
    if form.is_valid():
        form.save()
        return redirect("/complete")
    return render(request, 'gameregister/gameregisterform.html', {'form': form} )

def complete(request):
    return render(request, 'gameregister/complete.html')