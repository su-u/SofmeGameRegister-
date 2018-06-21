from django import forms
from .models import GameInfo
 
class GameInfoForm(forms.ModelForm):
    class Meta:
        model = GameInfo
        fields = ("name", "id", "discription", "gamefile")

        def clean_id(self):

            id = self.cleaned_data['id']

            if id < 0 or id > 50:
                raise forms.ValidationError('範囲外です。')

            return id
