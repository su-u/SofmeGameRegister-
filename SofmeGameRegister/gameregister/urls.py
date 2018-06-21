from django.conf.urls import url
from gameregister.views import GameInfoCreateView

app_name = 'register'

urlpatterns = [
    #url('^$', views.kakikomi, name='kakikomi'),
    url(r'^$', GameInfoCreateView.as_view()),
]