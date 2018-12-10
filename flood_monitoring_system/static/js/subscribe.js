$( document ).ready(function(){
	$('#form-msg').hide();
	$("#subscribe").click(function() {
		let msg = "";
        if(form_is_valid()){
        	let sent = false;
			let dataString =JSON.stringify({name: $("#name").val(),postcode: $("#postcode").val(),email: $("#email").val()})
			$.ajax({
			   url: "/subscription/",
			   type: "post",
			   timeout: 1000,
			   datatype: "json",
			   data: dataString,
			   async:false,
			   success: function (data) {
				   let d = $.parseJSON(data);
				   if(d.status){
					sent = true;
				   }
				   msg = d.msg
			   },
			    error: function(XMLHttpRequest, textStatus, errorThrown) {
			   	    msg = "Error whilst subscribing. Please try again later.";
				}
			});
            if(sent){
                $('#form-msg').addClass("list-group-item-success");
				$('#form-msg').removeClass("list-group-item-danger");
            }else{
				$('#form-msg').addClass("list-group-item-danger");
				$('#form-msg').removeClass("list-group-item-success");
			}
        }else{
			msg = "Please fill in the form correctly.";
			$('#form-msg').addClass("list-group-item-danger");
			$('#form-msg').removeClass("list-group-item-success");
		}
        $('#form-msg').text(msg);
		$('#form-msg').show();
    });

	$("#view-data-btn").click(function () {
		if(validatePostcode($(this))){
			$.ajax({
			   url: "/subscription/",
			   type: "post",
			   timeout: 1000,
			   datatype: "json",
			   data: dataString,
			   async:false,
			   success: function (data) {
				   let d = $.parseJSON(data);
				   console.log(d)
			   }
			});
		}
    });

	var timeoutId;
	$(document).on('keyup change', 'input',function() {
			clearTimeout(timeoutId);
			let input = $(this);
			timeoutId = setTimeout(function() {
				validate(input);
		}, 1000, input);
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



//VALIDATORS===================================================================
function form_is_valid(){
	let valid = true;
	let form = [$("#name"), $("#postcode"), $("#email")];
	for(let i = 0; i < form.length; i++){
		let item  = form[i];
		if(validate(item) == false){
			valid = false
		}
	}
	return valid;
}

function validate(item){
	let valid = true;
	let type = item.attr('id');
	if(type == "name"){
		if(!validateName(item)){
			valid = false;
			item.addClass("input-error");
		}else{
			item.removeClass("input-error");
		}
	}else if(type == "postcode"){
		if(!validatePostcode(item)){
			valid = false;
			item.addClass("input-error");
		}else{
			item.removeClass("input-error");
		}
	}else if(type == "email"){
		if(!validateEmail(item)){
			valid = false;
			item.addClass("input-error");
		}else{
			item.removeClass("input-error");
		}
	}
	return valid;
}

function validateEmail(item){
	let email = item.val();
	let re = new RegExp(/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/);
	return re.test(email);
}

function validatePostcode(item){
	let pc = item.val();
	if (pc !== null){
		pc = pc.toUpperCase();
		var re =  new RegExp("^([A-PR-UWYZ0-9][A-HK-Y0-9][AEHMNPRTVXY0-9]{0,1}[ABEHMNPRVWXY0-9]{0,1} {1,2}[0-9][ABD-HJLN-UW-Z]{2}|GIR 0AA)$");
		var re2 = new RegExp("^([A-PR-UWYZ0-9][A-HK-Y0-9][AEHMNPRTVXY0-9]?[ABEHMNPRVWXY0-9]? {0,2}[0-9][ABD-HJLN-UW-Z]{2}|GIR ?0AA)$");
		if(re.test(pc) || re2.test(pc)){
			return true;
		}
	}
	return false;
}

function validateName(item){
	let name = item.val();
	return name.length > 1;
}

function csrfSafeMethod(method) {
	return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}