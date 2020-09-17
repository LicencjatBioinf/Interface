from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import SearchForm
from WGraphPy import *
from .experimental import ReadInputFile
from .fasta_index import FastaIndexer



uniprot_path = "/home/shared/uniprot/uniprot_trembl.fasta"


class Home(TemplateView):
    template_name = 'index.html'


def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST, request.FILES)
        if form.is_valid():
            input_file = form.cleaned_data['spectrum_input_file']
            max_wasserstain_distance = form.cleaned_data['max_wasserstain_distance']
            theoretical_spectrum_coverage = form.cleaned_data['theoretical_spectrum_coverage']
            organism = form.cleaned_data['organism']
            search_area = form.cleaned_data['search_area']
            database = form.cleaned_data['database']
            fasta_input_file = form.cleaned_data['fasta_input_file']
            max_results = form.cleaned_data['max_results']
            enzymatic_activity = form.cleaned_data['enzymatic_activity']
            posttranslational_modifications = form.cleaned_data['posttranslational_modifications']

            #----------- Search area: Database -----------
           
            moja_lista = ReadInputFile(input_file) 
            mean_mass=sum(prob*mass for mass,prob in moja_lista)
            f = [(id.split("|")[1], seq) for id, seq in FastaIndexer(uniprot_path).search(
                mean_mass - max_wasserstain_distance, mean_mass + max_wasserstain_distance) if organism in id]



            liczba_pikow = len(moja_lista)
            try:
                results = wsearch(fastas=f, eksperymentalne=moja_lista, limit=max_wasserstain_distance,
                                  results_max_size=max_results,part_of_spectrum=theoretical_spectrum)
            
                protein_counter = len(results)
            
                return render(request, 'results.html', {
                    'protein_counter': protein_counter, 'liczba_pikow': liczba_pikow, 'results': results,
                    'lista': moja_lista})
            except:
                return render(request,'noresults.html')



    else:
        form = SearchForm()

    return render(request, 'index.html', {'form': form})

def about(request):
    return render(request, 'about.html')