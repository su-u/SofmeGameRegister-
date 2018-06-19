from django import forms
 
class GameForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    body = forms.CharField(widget=forms.Textarea)
    gamefile = forms.FileField()
