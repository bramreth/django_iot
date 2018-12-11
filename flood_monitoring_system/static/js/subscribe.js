let data= {};
let data_preview;
let view_data_btn;
let station_select;
$( document ).ready(function(){
	$.ajax({
	   url: "https://environment.data.gov.uk/flood-monitoring/id/stations?_limit=50",
	   async:false,
	   success: function (d) {
		  data = d.items;
	   }
	});

	station_select = $("#station-select");
	view_data_btn = $("#view-data-btn");
	data_preview = $("#data-preview");

	for(let i = 0; i< data.length; i++){
        station_select.append(new Option(data[i].label, data[i].RLOIid));
    }
	//SORT-----------------------------------------------
	var options = $('#station-select option');
	let arr = options.map(function(_, o) {
        return {
            t: $(o).text(),
            v: o.value
        };
    }).get();
	arr.sort(function(o1, o2) {
        return o1.t > o2.t ? 1 : o1.t < o2.t ? -1 : 0;
    });
    options.each(function(i, o) {
        o.value = arr[i].v;
        $(o).text(arr[i].t);
    });
    //--------------------------------------------------

	//BUTTON LISTENERS
    view_data_btn.click(function() {
    	data_preview.empty();
	  id = station_select.val();
	  item = {};
	  for(let i = 0; i< data.length; i++){
         if(data[i].RLOIid == id){
         	item = data[i];
		 }
	  }
       for (var k in item) {
       	data_preview.append("<li class='list-group-item'><b>"+k+":</b> "+item[k]+"</li>");
       }
	});

    $( document).on( "click", ".del-btn" ,function() {
		//if accepted
		var btn = $(this);
		if (confirm('Are you sure you want unsubscribe from this station?')) {
			let dataString =JSON.stringify({station: $(this).attr("station")})
			$.ajax({
			   url: "/unsub/",
			   type: "post",
			   timeout: 1000,
			   datatype: "json",
			   data: dataString,
				success: function(d){
			   		d = $.parseJSON(d);
					console.log(d.status);
					if(d.status){
						let wanted = btn.parent().parent();
    					if (wanted.hasClass('row')) wanted.remove();
					}
				}
			});
		}
	});

    var csrftoken = $.cookie('csrftoken');
	$.ajaxSetup({
		beforeSend: function(xhr, settings) {
			if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		}
    });
	$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
    });
});

function csrfSafeMethod(method) {
	return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}