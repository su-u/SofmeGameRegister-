from django.shortcuts import render
from django.http import HttpResponse
from gameregister.forms import GameForm
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.conf import settings
from gameregister.models import FileNameModel
import sys, os
UPLOADE_DIR = os.path.dirname(os.path.abspath(__file__)) + '/static/files/'

def kakikomi(request):
    #if request.method != 'POST':
    f = GameForm()
    return render(request, 'gameregister/gameregisterform.html', {'form1': f} )

    #file = request.POST['file']
    #path = os.path.join(UPLOADE_DIR, file.name)
    #destination = open(path, 'wb')

    #for chunk in file.chunks():
    #    destination.write(chunk)

    #insert_data = FileNameModel(file_name = file.name)
    #insert_data.save()
