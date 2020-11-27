var przymiotniki = ["Miły", "Brzydki", "Przystojny", "Obleśny", "Niemiły", "Postępowy", "Krnąbrny", "Zadufany", "Uległy", "Spięty", "Nieufny", "Samolubny","Niski","Wysoki","Gruby","Chudy"];
var kto = ["szambonurek", "pilot", "złomiarz", "sąsiad", "kelner", "ogrodnik", "prezydent", "szef", "informatyk", "kierowca", "żul", "magik","piłkarz","dzieciak","przewodnik",""];
var czasowniki = ["sprzątał", "programował", "kopnął", "zgubił", "znalazł", "porzucił", "olał", "zapalił", "połknął", "kupił", "spalił", "gonił","skonstruował","pożyczył","wyrzucił","zepsuł"];
var rzeczowniki =["żonę", "grę", "dom", "kosz", "pieniądze", "szefa", "papierosy", "tabletkę", "auto", "dokumenty", "auto", "samolot","dziecko","narkotyki","wódke"];

window.onload = load;

function load()
{
	for(i = 0; i < 15; i++)
	{
		$('<p>').text(przymiotniki[i]).appendTo($('#przymiotniki'));
		$('<p>').text(kto[i]).appendTo($('#kto'));
		$('<p>').text(czasowniki[i]).appendTo($('#czasowniki'));
		$('<p>').text(rzeczowniki[i]).appendTo($('#rzeczowniki'));
	}
}

$('#guzik').click(function () {
	generate();
});

function generate(){
	var w1 = przymiotniki[Math.floor(Math.random()*15)];
	var w2 = kto[Math.floor(Math.random()*15)];
	var w3 = czasowniki[Math.floor(Math.random()*15)];
	var w4 = rzeczowniki[Math.floor(Math.random()*15)];
	
	var text = w1+" "+w2+" "+w3+" "+w4;
	$('#zdanie').val(text);
}
