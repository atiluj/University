$('#searchphrase').on('input', function() {
	
	var findText_length = $('#searchphrase').val().length;
	clean();
	
		if(findText_length < 3)
	{	
		$('ul').addClass('notfound');
		if(findText_length == 0) $('ul').removeClass('notfound');
	}	
	else
	{
		search();
	}	
})

function clean()
{
	$('li').html(function(_, html){
    return html.replace('<mark>', "");
	});
	
	$('li').html(function(_, html){
    return html.replace('</mark>', "");
    });
}

function search()
{
	var findText = $('#searchphrase').val();
	$('li').each(function() {
		if($(this).text().includes(findText)){
			var text = $(this).text();
			$(this).html(text.replace(findText, '<mark>'+findText+'</mark>')); 
        }
	})
}