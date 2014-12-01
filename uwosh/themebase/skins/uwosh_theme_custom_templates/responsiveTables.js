/*! A responsive table solution written by mad Jquery expert  David Hietpas, from the University of Wisconsin Oshkosh*/

// Continuously run at defined interval below

var COLSPAN_CLASS = 'colspan-table-head';
var HEADING_CLASS = 'td-table-head';
var SIZE_SWITCH = 770;
var tableResizeThread = null;
var tableRestoreThread = null;

function resizeTables(){

	if($(window).width() <= SIZE_SWITCH){
   	$('table').each(function(i,table){
      	var colspan_heading = null;
      	var headings = [];
      	$(table).find('th').each(function(j,th){
          	if(!$(th).is("[colspan]"))
            	headings.push($(th).text());
          	else
            	colspan_heading = $(th).text();
      	});
     	 
      	if(headings.length == 0)
          	return false;

      	$(table).find('tr').each(function(k,tr){
           	jq(tr).find('td').each(function(l,td){
               	var span = $('<span>').addClass(HEADING_CLASS).html(headings[l]);
               	var temp = $(td).html();
               	$(td).html(span);
               	$(td).append(temp);
           	});
      	});
       	 
      	if(colspan_heading != null) {
         	var h2 = $('<h2>').addClass(COLSPAN_CLASS).html(colspan_heading);
         	$(table).parent().prepend(h2);
      	}
     	 
   	});
  	 

   	// Destroy Thread
   	newRestoreThread();
   	clearInterval(tableResizeThread);
   	tableResizeThread = null;

	}

}

function restoreTables() {

	// If resized up remove all elements with HEADING_CLASS marker.  This will purge the headings in the <td> elements
	if($(window).width() > SIZE_SWITCH) {
   	$('.' + HEADING_CLASS).remove();
   	$('.' + COLSPAN_CLASS).remove();

   	// Destroy Thread
   	newResizeThread();
   	clearInterval(tableRestoreThread);
   	tableRestoreThread = null;
	}

}


function newResizeThread() {

	tableResizeThread = setInterval(function(){
   	resizeTables();
	},
	250);

}

function newRestoreThread() {

	tableRestoreThread = setInterval(function(){
   	restoreTables();
	},
	250);

}

// Start Thread Listener
newResizeThread();



