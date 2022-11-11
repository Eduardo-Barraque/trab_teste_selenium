from django import forms



class UserForm(forms.Form):
    peso = forms.FloatField()
    altura = forms.FloatField()
    sexo = forms.CharField()
