from pyteomics import mzxml
import numpy as np

def ReadInputFile(file):
    """Funkcja jako argument przyjmuje plik mzxml z 1 widmem eksperymentalnym, 
    zwraca liste tupli [(masa1, pstwo1),...,(masaN, pstwoN)]"""
    with mzxml.read(file) as reader:
        mz_and_intensity = []
        for spectrum in reader:
            intensity = spectrum['intensity array']
            intensity_sum = np.sum(intensity)
            peaks_count = spectrum['peaksCount']
            for p in range(peaks_count):
                prob = spectrum['intensity array'][p]/intensity_sum
                mz_and_intensity.append((spectrum['m/z array'][p], prob))
    return(mz_and_intensity)