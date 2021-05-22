from django import forms

class RatingForm(forms.Form):
    id = forms.CharField(max_length=1000)
    url = forms.URLField(max_length=1000)
