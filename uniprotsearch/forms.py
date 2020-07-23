from django import forms

class Form(forms.Form):
    name = forms.CharField()
    input_file = forms.FileField()
    max_distance = forms.FloatField()
    theoretical_spectrum = forms.FloatField()
    organizm = forms.CharField()
    send_by_email = forms.BooleanField()
    email = forms.EmailField()
