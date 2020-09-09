from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import SearchForm
from django.core.mail import send_mail
from WGraphPy import *
from .experimental import ReadInputFile
from .fasta_index import FastaIndexer

#uniprot_path = "/home/shared/uniprot/uniprot_trembl.fasta"


class Home(TemplateView):
    template_name = 'index.html'


def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST, request.FILES)
        if form.is_valid():
            input_file = form.cleaned_data['input_file']
            max_wasserstain_distance = form.cleaned_data['max_wasserstain_distance']
            max_results = form.cleaned_data['max_results']

            moja_lista = ReadInputFile(input_file)
            mean_mass = sum([prob * mass for prob, mass in moja_lista])
            print(mean_mass, "to  srednia masa, to krotki: ", moja_lista)
            #f = [(id, seq) for id, seq in FastaIndexer(uniprot_path).search(
            #    mean_mass - max_wasserstain_distance, mean_mass + max_wasserstain_distance)]
            path = "C:/Users/LaptopHP/Dropbox/studia/III rok sem letni/Praca licencjacka/WGraphPy/tests/uniprot-mass_[900+TO+1100].fasta"

            f = fasta_reader(path)
            print("zaladowano ", len(f), " bialek")
            protein_counter = len(f)

            liczba_pikow = len(moja_lista)

            results = wsearch(fastas=f, eksperymentalne=moja_lista, limit=max_wasserstain_distance,
                              results_max_size=max_results)

            return render(request, 'results.html', {
                'protein_counter': protein_counter, 'liczba_pikow': liczba_pikow, 'results': results,
                'lista': moja_lista})

    else:
        form = SearchForm()

    return render(request, 'index.html', {'form': form})
