from django import forms

class SearchForm(forms.Form):
    #name = forms.CharField()
    spectrum_input_file = forms.FileField()
    max_wasserstain_distance = forms.FloatField(label=('Max Wasserstain distace'), initial=0.5)
    theoretical_spectrum_coverage = forms.FloatField(initial=0.98, min_value=0.0, max_value=1.0)
    organism = forms.CharField(required=False, label=('Organism (optional)'))
    DATABASES= [
        ('1', 'TrEMBL'),
        ('2', 'Swiss-Prot'),
        ('3', 'UniProt'),
    ]
    MODIFICATIONS = [
        ('1', 'methylation'),
        ('2', 'acetylation'),
        ('3', 'hydroxylation'),
        ('4', 'phosphorylation'),
        ('5', 'glycosylation'),
        ('6', 'ubiquitination'),
        ('7', 'S-nitrosylation'),
        ('8', 'N-acetylation'),
        ('9', 'lipidation'),
    ]

    SEARCH_AREAS = [
        ('1', 'database'),
        ('2', 'your own fasta file'),

    ]
    search_area = forms.ChoiceField(choices=SEARCH_AREAS, widget=forms.RadioSelect(attrs={'onclick':"myFunction()"}))
    database = forms.ChoiceField(widget=forms.Select, choices=DATABASES)
    fasta_input_file = forms.FileField(required=False)

    max_results = forms.IntegerField(label=('Maximum number of proteins in the result'), initial=25)

    ENZYMATIC_ACTIVITY = [
        ('1', 'yes'),
        ('2', 'no'),
    ]
    enzymatic_activity = forms.ChoiceField(choices=ENZYMATIC_ACTIVITY, widget=forms.RadioSelect, required=False)
    posttranslational_modifications = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple, choices=MODIFICATIONS,)

    #send_by_email = forms.BooleanField()
    #email = forms.EmailField()
