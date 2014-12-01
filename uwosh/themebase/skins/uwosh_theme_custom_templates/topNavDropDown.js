function below_977_yes(){
   jQuery("#top_level_navigation").prepend('<button type="button" class="top-navigation-button">UWO Navigation</button>');
    jQuery('button.top-navigation-button').bind('click', function() {
       jQuery('ul#topNav').toggleClass('expanded');
       }); 
    jQuery("button.top-navigation-button").toggle(function()  {  
       jQuery(this).text("Hide Navigation");  
       },  
       function() {  
        jQuery(this).text("Show Navigation"); 
       }  
       );
     }


jQuery(document).ready(function() {
       if ( jQuery(".top-navigation-button").length == 0 ) {
          
       
       // If the window starts out at 977px or below put in the button and hide the nav
        if (jQuery(window).width() <= 977) {
             below_977_yes();
        }
}
        jQuery(window).resize(function() {
           // When the window is resized and it is at or below 977px put in the button and hide the nav
            if (jQuery(window).width() <= 977) { 
                if ( jQuery(".top-navigation-button").length == 0 ) {
                   below_977_yes(); 
                 }
             } 
            // When the window is resized and it is above 977 take away the buttons and put the nav back to normal
            if (jQuery(window).width() > 977) {
                 if ( jQuery(".top-navigation-button").length > 0 ) {
                     jQuery('.top-navigation-button').remove();
                }
                 jQuery('ul#topNav').removeClass('expanded');
            }
           });

        });
