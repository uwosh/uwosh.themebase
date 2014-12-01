
jq(document).ready(function(){
    
    //Start search stuff here
	var portal_search = "#portal-searchbox";
	var google_search = "#google-searchbox";
	var campus_checkbox = "#portal-searchbox-checkbox-campus";
	var site_checkbox = "#portal-searchbox-checkbox-site";
	var portal_search_input = "#portal-searchbox input[type=text]";
	var google_search_input = "#google-searchbox input[type=text]";	
	
	function enable_google_search(){
		jq(portal_search).hide();
		jq(google_search).show();
		//jq(google_search_input).attr('value', jq(portal_search_input).attr('value'));
	};
	
	function enable_site_search(){
		jq(google_search).hide();
		jq(portal_search).show();
		jq(portal_search_input).attr('value', jq(google_search_input).attr('value'));
	};
	
	jq(campus_checkbox).click(function(){
		if(jq(this).attr('checked')){
			enable_google_search();
			jq(site_checkbox).attr('checked', true);						
		}else{
			enable_site_search();
			jq(site_checkbox).attr('checked', false);
		}
	});
	jq(site_checkbox).click(function(){
		if(jq(this).attr('checked')){
			enable_google_search();
			jq(campus_checkbox).attr('checked', true);
		}else{
			enable_site_search();
			jq(campus_checkbox).attr('checked', false);
		}
	});
	//end search config stuff
	
	//cool little titan services hover
        jq('#titanServicesLink').hover(
	    function(){//over
		jq("#titanServicesLinks").fadeIn(300);
	    },
	    function(){//out
		jq("#titanServicesLinks").fadeOut(200);
	    }
        ); 
    //end titan services stuff
    
    //IE6 background image 
    try{
        document.execCommand("BackgroundImageCache", false, true);
    }catch(e){
        //do nothing... just want to catch potential problems
    }
    
});
