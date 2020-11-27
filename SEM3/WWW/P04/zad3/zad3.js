$('.photo').click(function() { //co się stanie po kliknięciu na zdjęcie
    if($(this).data("marked") == false){
		//zaznaczenie zdjęcia		
        markPhoto($(this));
    }else{
		//odznaczenie zdjęcia
        unmarkPhoto($(this));
    }
  });

function markPhoto(nr) //zaznczenie zdjęcia
{
	nr.addClass('photoA'); //dodanie nowej klasy
	nr.removeClass('photo');
	nr.data("marked", true);
	markedPhotos();
}

function unmarkPhoto(nr) //odznaczenie zdjęcia
{
	nr.addClass('photo'); //dodanie nowej klasy
	nr.removeClass('photoA');
	nr.data("marked", false);
	markedPhotos();
}

$('#guzik').click(function() {
	 if($(this).data("marked") == false){
        //zaznacz 
		markAll();
		$('#guzik').data("marked", true);
    }
	else{
        //odznacz wszystkie
	    unmarkAll();
		$('#guzik').data("marked", false);
	}
});

$('#guzik2').click(function() {
	var pliki = '';
	$('.photoA').each(function() {
		pliki = pliki + $(this).attr('id')+".png \n \n" ; 
	})
	$('#log').val(pliki);
	console.log(pliki);	
});

function markAll()
{
	$('.photo').each(function() {markPhoto($(this)) });
}

function unmarkAll()
{
	$('.photoA').each(function() {unmarkPhoto($(this)) });
}

function markedPhotos() //lista zaznaczonych zdjęć
{
	var pliki = '';
	$('.photoA').each(function() {
		pliki = pliki + $(this).attr('id')+".png \n \n" ; 
	})
	$('#log').val(pliki);
}