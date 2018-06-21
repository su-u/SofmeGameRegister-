from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.views.generic import CreateView, UpdateView

from .models import GameInfo
from .forms import GameInfoForm

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


class GameInfoCreateView(CreateView):
    model = GameInfo
    form_class = GameInfoForm
    template_name = "gameregister/gameregisterform.html"
    success_url = "/"  # 成功時にリダイレクトするURL