$( function() {
	var dialog;
	var dialog2;
	var form; 
	var name = $( "#name" );
	var surname = $( "#surname" );
	var city = $( "#city" );
	var code = $( "#code" );
	var birth_date = $( "#birth_date" );
	var element_delete;
	
	$( "#birth_date" ).datepicker();

	function addUser() {
		$( "#user tbody" ).append( "<tr class=\"data\"> <td>" + name.val() + "</td>" + //bierze zawartośc tabelki
													 "<td>" + surname.val() + "</td>" +
													 "<td>" + city.val() + "</td>" +
													 "<td>" + code.val() + "</td>" +
													 "<td>" + birth_date.val() + "</td>" +
													 "<td> <button class=\"delete\">USUŃ</button> </td></tr>" );
		$( ".delete" ).on( "click", function() {
			element_delete = this;
			dialog2.dialog( "open" );
		});
		dialog.dialog( "close" );	//zamknięcie okna
		return true;
	}
	
	function deleteUser(event){
		
		var to_delete = element_delete.parentElement.parentElement;
		to_delete.parentNode.removeChild(to_delete);
		dialog2.dialog( "close" );	//zamknięcie okna
		return true;
	}
	 
	dialog = $( "#new_user" ).dialog({
		autoOpen: false, //otwarcie pyrz załadowaniu strony
		height: 400,
		width: 410,
		modal: true, 
		buttons: { //guziki w okienku
			Zapisz: addUser,
			Anuluj: function() {
			dialog.dialog( "close" );
			}
		},
		close: function() { //zamknięcie i wyczyszczenie formularzu
			form[ 0 ].reset();
		}
	});
	
	dialog2 = $( "#delete_user" ).dialog({
		autoOpen: false, //otwarcie pyrz załadowaniu strony
		height: 200,
		width: 270,
		modal: true, 
		buttons: { //guziki w okienku
			Usuń: deleteUser,
			Anuluj: function() {
			dialog2.dialog( "close" );
			}
		}
	});
	 
	form = dialog.find( "form" ).on( "submit", function( event ) { 
	  event.preventDefault();
	  addUser();
	});
	 
	$( "#save_user").on( "click", function() {
	  dialog.dialog( "open" );
	});
	
	$( ".delete" ).on( "click", function() {
		element_delete = this;
	    dialog2.dialog( "open" );
	});
});
