function myFunction() {
    var a = document.activeElement;// activeElement
    var d = document.getElementsByClassName("database-div")[0];
    var f = document.getElementsByClassName("fasta_input_file-div")[0];
    if (a.value == 1) {
        d.style.display = "block";
        f.style.display = "none";
    }
    if (a.value == 2) {
        d.style.display = "none";
        f.style.display = "block";
    }                
}

// Informacje w dymkach, które wyświetlają się po najechaniu na ikonkę informacyjną.
(function ($) {
    $(document).ready(function(){
    $("#spectrum_input_file-span").text("Upload a file with non-fragmented spectrum in mzXML format.");
    $("#max_wasserstain_distance-span").text("Specify the maximum Wasserstain distance.");
    $("#theoretical_spectrum_coverage-span").text("A fraction specifying what part of the theoretical spectrum will be generated. The unit: %.");
    $("#organism-span").text("Only this group will be searched.");
    $("#search_area-span").text("Specify the search source.");
    $("#database-span").text("Select the name of the public database.");
    $("#fasta_input_file-span").text("Upload your own file in fasta format.");
    $("#max_results-span").text("Specify the maximum number of results that will appear on the page.");
    $("#enzymatic_activity-span").text("Determining if a protein has enzymatic activity. Attention! It doesn't work yet! We will add this functionality soon.");
    $("#posttranslational_modifications-span").text("Choose post-translational modifications. Attention! It doesn't work yet! We will add this functionality soon.");
    });
}(jQuery))