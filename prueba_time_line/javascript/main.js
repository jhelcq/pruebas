var mapa = new google.maps.Map( $('.map').get(0) , {
  center: { lat: -16.7638, lng: -68.8482},
  zoom: 5,
    streetViewControl: false
});

//----- eventos para timeline -----
$('.redondos').click(function(){
	alert('click en anio')
})

$('#desplazador_izquierda').click( function(){
	var margin= parseInt($('.contenedor_redondos').css('margin-left').replace('px', '')); 
	$('.contenedor_redondos').css('margin-left', (margin- 10) + 'px');
})

$('#desplazador_derecha').click( function(){
	var margin= parseInt($('.contenedor_redondos').css('margin-left').replace('px', '')); 
	$('.contenedor_redondos').css('margin-left', (margin+ 10) + 'px');
})
