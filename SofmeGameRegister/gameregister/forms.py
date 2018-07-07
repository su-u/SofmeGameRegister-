from django import forms
from .models import GameInfo
 
class GameInfoForm(forms.ModelForm):
    class Meta:
        model = GameInfo
        fields = ["name", "representative", "game_id", "discription", "gamefile", "panel", "movie"]
