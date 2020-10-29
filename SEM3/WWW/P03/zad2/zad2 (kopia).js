window.onload = load; //ma sie odpalic od razu

function addMarkaOnStart(nazwa) {
    var selectMenu = document.getElementById("marka"); //od do obiektu select z id="marka"
    var optionToAdd = document.createElement("option"); 
	
    optionToAdd.appendChild( document.createTextNode(nazwa));
    optionToAdd.value = nazwa; 
    selectMenu.appendChild(optionToAdd);
}

function addModelOnStart(markaNazwa, modelNazwa)
{
    var selectMenu = document.getElementById("model");
    var optionToAdd = document.createElement("option");

    optionToAdd.appendChild( document.createTextNode(modelNazwa));
    optionToAdd.value = markaNazwa; //<option value="Skoda">Fabia</option>
    selectMenu.appendChild(optionToAdd);

    var newElems = selectMenu.querySelectorAll('option');
    var elems = Array.prototype.slice.call(newElems);

    list.push.apply(list, elems);
}

function load() {
	
    addMarkaOnStart("Fiat");
    addMarkaOnStart("Ford");
    addModelOnStart("Fiat", "Tipo");
    addModelOnStart("Fiat", "500");
    addModelOnStart("Ford", "Focus");
    addModelOnStart("Ford", "Mondeo");
    giveSelection(sel1.value); //na początku odpalenia strony to pokazuje dla domyślnej(pierwszej) marki modele //inaczej dla jednej marki bylyby 
}

function addElem(){
    var markaRadioCheck = document.getElementById("markaRadio").checked;

    if(markaRadioCheck == true) { //dodanie marki
        var selectMenu = document.getElementById("marka"); //odnośnik do znacznika z id="marka"
        //var selectMenuValue = selectMenu.value;
        var optionToAdd = document.createElement("option"); //stworzenie taga o znaczniku option
        var optionTextToAdd = document.getElementById("nowa").value;

        optionToAdd.appendChild( document.createTextNode(optionTextToAdd));
        optionToAdd.value = optionTextToAdd; //<option value="Skoda">Skoda</option>
        selectMenu.appendChild(optionToAdd); //dodanie
    } else { //dodanie modelu
        var selectMenu = document.getElementById("model"); //odnośnik do znacznika z id="model"
        var markaValue = document.getElementById("marka").value; //wyciągamy marke tego modelu
        var optionToAdd = document.createElement("option"); //stworzenie taga o znaczniku option
        var optionTextToAdd = document.getElementById("nowa").value;

        optionToAdd.appendChild( document.createTextNode(optionTextToAdd));
        optionToAdd.value = markaValue; //<option value="Skoda">Fabia</option>
        selectMenu.appendChild(optionToAdd); //dodanie

        var newElems = selectMenu.querySelectorAll("option"); //lista wszystkich znaczników option
        var elems = Array.prototype.slice.call(newElems); //zamiana typu listy

        list.push.apply(list, elems);
    }
}

var sel1 = document.getElementById("marka"); //odnośnik do znacznika select w dokumencie html z id=marka
var sel2 = document.getElementById("model"); //odnośnik do znacznika select w dokumencie html z id=model 
var options2 = sel2.querySelectorAll("option");//przechowuje znaczniki option i wszystkie informacje powiązane z nimi
var list = Array.prototype.slice.call(options2);//options2 - typ Node list (czyli nie możemy jej edytować) czyli poprostu zamian typu ||| <option value="Ford">Focus</option>

function giveSelection(selValue) {
    sel2.innerHTML =""; //czyści opcje modeli dla nowej marki
    for(var i = 0; i < list.length; i++) {
        if(list[i].value === selValue) {
			sel2.appendChild(list[i]);
		}
    }
}

giveSelection(sel1.value);

