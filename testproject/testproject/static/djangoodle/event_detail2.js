function my_js_callback(data){
                window.console.log(data);
                $("#participants").append("<p>" + data.name + "</p>");
                $("#id_name").val("");
            }