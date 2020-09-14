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