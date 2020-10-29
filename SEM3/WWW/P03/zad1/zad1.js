function checkNumAccount(){
	var PatternAccount = new RegExp(/\d{26}/);
	var nr_konta= document.getElementById("nr_konta").value;
	
	if(!PatternAccount.test(nr_konta)) alert("NIEPOPRAWNY NUMER KONTA! \n Numer konta składa się z 26 cyfr.");
}

function checkPesel(){
	var PatternPesel = new RegExp(/\d{11}/);
	var pesel = document.getElementById("pesel").value;
	
	if(!PatternPesel.test(pesel)) alert("NIEPOPRAWNY NUMER PESEL! \n Pesel składa się z 11 cyfr.");
	
}

function checkDate(){
	var PatternDate = new RegExp(/\d{4}([-]\d{2})([-]\d{2})/);
	var data= document.getElementById("data").value;
	
	if(!PatternDate.test(data)) alert("NIEPOPRAWNA DATA! \n Poprawna konstrukcja dd-mm-rrrr. Data zawiera tylko liczby!");
}

function checkMail(){
	var PatternMail = new RegExp(/^\S+@\S+\.\S+$/);
	var mail = document.getElementById("mail").value;
	
	if(!PatternMail.test(mail)) alert("NIEPOPRAWNY MAIL! ");
}

function checkAll(){
	checkNumAccount()
	checkPesel()
	checkDate()
	checkMail()
}

var nr_konta = document.getElementById("nr_konta");
nr_konta.addEventListener('focusout', (event) => {
    checkNumAccount();
});

var pesel = document.getElementById("pesel");
pesel.addEventListener('focusout', (event) => {
    checkPesel();
});

var data = document.getElementById("data");
data.addEventListener('focusout', (event) => {
    checkDate();
});

var mail = document.getElementById("mail");
mail.addEventListener('focusout', (event) => {
    checkMail();
});

var button = document.getElementById("button");
button.addEventListener('click', (event) => {
    checkAll();
});

