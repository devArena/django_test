function add_participant_callback(data){
                window.console.log(data);
                $("#participants").append("<p>" + data.name + "</p>");
                $("#id_name").val("");
            }

function add_participant(event_id) {
	Dajaxice.djangoodle.add_participant(add_participant_callback,
										{'form':$('#input_form').serialize(true),
										 'event_id':event_id
										});
}