from django import forms

class link(forms.Form):
    link = forms.CharField(max_length=300)

