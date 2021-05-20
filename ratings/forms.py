from django import forms

class RatingForm(forms.Form):
    url = forms.URLField(max_length=1000)
