/*!
 * Meta Jersey by Team Deep Purple
 */
 
 (function($)
 {
	 "use strict";
	 
	 $('a.page-scroll').bind('click', function(event)
	 {
		 var $anchor = $(this);
		 $('html, body').stop().animate(
			 {
				 scrollTop: ($($anchor.attr('href')).offset().top - 50)
			 }, 1250, 'easeInOutExpo');
			 
			 event.preventDefault();
	 });
	 
	 
	 $('.navbar-collapse ul li a').click(function()
	 {
		 $('.navbar-toggle:visible').click();
	 });
	 
	 $('body').scrollspy(
		 {
			 target: '.navbar-fixed-top',
			 offset: 51
		 })
		 
	$(document).ready(function() {
    $('#table').dataTable({
        "aLengthMenu": [[25, 50, 75, -1], [25, 50, 75, "All"]],
        "iDisplayLength": 25
    	});
	} );	 	 
 })(jQuery); 