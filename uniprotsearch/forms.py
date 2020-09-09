from django import forms

class SearchForm(forms.Form):
    #name = forms.CharField()
    input_file = forms.FileField()
    max_wasserstain_distance = forms.FloatField(label=('Max Wasserstain distace'))
    #theoretical_spectrum = forms.FloatField()
    max_results = forms.IntegerField(label=('Maximum number of proteins in the result'))
    #organizm = forms.CharField()
    #send_by_email = forms.BooleanField()
    #email = forms.EmailField()
