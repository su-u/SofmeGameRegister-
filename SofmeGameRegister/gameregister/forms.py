from django import forms
from .models import GameInfo
 
class GameInfoForm(forms.ModelForm):
    class Meta:
        model = GameInfo
        fields = ["name", "representative", "game_id", "discription", "gamefile",
                 "panel","picture_1","picture_2","picture_3" ,"movie"]
        widgets = {
            "gamefile": forms.TextInput(attrs={"type":"file","onchange": "$('#fake_text_box').val($(this).val())", "id": "gamefile",
                                               "style": "display:none;"})
        }

