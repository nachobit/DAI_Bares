jQuery(function($) {'use strict';

	//Responsive Nav
	$('li.dropdown').find('.fa-angle-down').each(function(){
		$(this).on('click', function(){
			if( $(window).width() < 768 ) {
				$(this).parent().next().slideToggle();
			}
			return false;
		});
	});

	//Fit Vids
	if( $('#video-container').length ) {
		$("#video-container").fitVids();
	}

	//Initiat WOW JS
	new WOW().init();

	// portfolio filter
	$(window).load(function(){

		$('.main-slider').addClass('animate-in');
		$('.preloader').remove();
		//End Preloader

		if( $('.masonery_area').length ) {
			$('.masonery_area').masonry();//Masonry
		}

		var $portfolio_selectors = $('.portfolio-filter >li>a');
		
		if($portfolio_selectors.length) {
			
			var $portfolio = $('.portfolio-items');
			$portfolio.isotope({
				itemSelector : '.portfolio-item',
				layoutMode : 'fitRows'
			});
			
			$portfolio_selectors.on('click', function(){
				$portfolio_selectors.removeClass('active');
				$(this).addClass('active');
				var selector = $(this).attr('data-filter');
				$portfolio.isotope({ filter: selector });
				return false;
			});
		}

	});


	$('.timer').each(count);
	function count(options) {
		var $this = $(this);
		options = $.extend({}, options || {}, $this.data('countToOptions') || {});
		$this.countTo(options);
	}
		
	// Search
	$('.fa-search').on('click', function() {
		$('.field-toggle').fadeToggle(200);
	});

	// Contact form
	var form = $('#main-contact-form');
	form.submit(function(event){
		event.preventDefault();
		var form_status = $('<div class="form_status"></div>');
		$.ajax({
			url: $(this).attr('action'),
			beforeSend: function(){
				form.prepend( form_status.html('<p><i class="fa fa-spinner fa-spin"></i> Email is sending...</p>').fadeIn() );
			}
		}).done(function(data){
			form_status.html('<p class="text-success">Thank you for contact us. As early as possible  we will contact you</p>').delay(3000).fadeOut();
		});
	});

	// Progress Bar
	$.each($('div.progress-bar'),function(){
		$(this).css('width', $(this).attr('data-transition')+'%');
	});

	if( $('#gmap').length ) {
		var map;

		map = new GMaps({
			el: '#gmap',
			lat: 43.04446,
			lng: -76.130791,
			scrollwheel:false,
			zoom: 16,
			zoomControl : false,
			panControl : false,
			streetViewControl : false,
			mapTypeControl: false,
			overviewMapControl: false,
			clickable: false
		});

		map.addMarker({
			lat: 43.04446,
			lng: -76.130791,
			animation: google.maps.Animation.DROP,
			verticalAlign: 'bottom',
			horizontalAlign: 'center',
			backgroundColor: '#3e8bff',
		});
	}

});


/*BOTONES TAMANIO LETRA*/
$(document).ready(function(){  
$('#botones .boton').click(function(){ /*al hacer click en un botón*/  
$('body').removeClass();    /*borre todas las clases*/  
if(this.id == 'aumentar'){   /*si la clase botón tiene el ID aumentar*/  
    $('body').addClass('grande');  /*cargue desde el CSS la clase grande*/  
    }  
else if(this.id == 'disminuir'){ /*si el ID es disminuir*/  
    $('body').addClass('chica'); /*cargue la clase chica*/  
}  
$('#botones .boton').removeClass('seleccion'); /*elimine la negrita del boton*/  
    $(this).addClass('seleccion');/*agregue la negrita al botón activo*/  
 });                             
});  
  
/*EFECTO HOVER*/  
$(document).ready(function() {  
  $('#botones .boton').hover(function() {  
    $(this).addClass('sobre'); /*agregue efecto hover*/  
  }, function() {  
    $(this).removeClass('sobre');  /*quite efecto hover*/  
  });  
}); 


/*EMERGENTES LOGIN/REGISTRO*/
$(document).ready(function(){
	$("#b2").click(function() {
	    $("#dialogo2").dialog({
	            width: 590,
	            height: 350,
	            show: "scale",
	            hide: "scale",
	            resizable: "false",
	            position: "center"     
	    });
    });
 });



$("#modal_trigger").leanModal({
        top: 100,
        overlay: 0.6,
        closeButton: ".modal_close"
});

$(function() {
        // Calling Login Form
        $("#login_form").click(function() {
                $(".social_login").hide();
                $(".user_login").show();
                return false;
        });

        // Calling Register Form
        $("#register_form").click(function() {
                $(".social_login").hide();
                $(".user_register").show();
                $(".header_title").text('Register');
                return false;
        });

        // Going back to Social Forms
        $(".back_btn").click(function() {
                $(".user_login").hide();
                $(".user_register").hide();
                $(".social_login").show();
                $(".header_title").text('Login');
                return false;
        });
});


          
$(function(){          
	$.ajax({
        url: "{% url 'reclama_datos' %}",
        type: 'get',                        
        success: function(datos) {
            Visualiza_datos (datos);  
        },
        failure: function(datos) { 
            alert('esto no vá');
        }
    });
});

/*GRAFICOS*/
$(function Visualiza_datos() {
	var bares=[];
    var vis=[];
        
    bares =  datos['bares'];
    visitas = datos['visitas'];

    $('#container').highcharts({
        chart: {
            type: 'bar'
        },
        title: {
            text: 'Visitas de cada bar'
        },
        xAxis: {
            categories: bares
        },
        yAxis: {
            title: {
                text: 'Nº visitas'
            }
        },
        series: [{
            name: 'Bares',
            data: visitas
        }],
    });
}); 