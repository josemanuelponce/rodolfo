var form = document.getElementById("createForm");

const tittle = document.getElementById("tittle_input");
const genres = document.getElementById("genres_input");
const authors = document.getElementById("authors_input");

var clearButton = document.getElementById("clearButton");
var hideButton = document.getElementById("hideButton");
var showButton = document.getElementById("showButton");

function onSubmitClicked(event) {
    if(tittle.value.trim().length === 0) {
        tittle.classList.add("error");
        alert("Tittle required");
        return false;
    } else {
        tittle.classList.remove("error");
    }

    if(genres.value.trim().length === 0) {
        genres.classList.add("error");
        alert("genres required");
        return false;
    } 

    if(authors.value.trim().length === 0) {
        authors.classList.add("error");
        alert("authors required");
        return false;
    } 

    return false;
}

function clear(){
    tittle.value = "";
    genres.value = "";
    authors.value = "";
}

function hide() {
    form.style.display = "none";
}

function show(){
    form.style.display = "";
}

// form.onsubmit = onSubmitClicked;

 clearButton.onclick = clear;
 hideButton.onclick = hide;
 showButton.onclick = show;