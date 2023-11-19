$(function () {

    $(document).ready(function() {
        getProgram();
    });

   $('#json_switch').change(function() {
       getProgram();
   });

    function getProgram() {
	console.log("Getting Program")
        var my_content_type = "text/plain"
        var my_headers = {
                          Accept: "text/plain; charset=utf-8",
                          "Content-Type": "text/plain; charset=utf-8"
            }
        if ($('#json_switch').prop("checked")) {
            my_content_type = "application/json"
            my_headers = {
                          Accept: "application/json",
                          "Content-Type": "application/json"
	    }
	}
        if ($('#json_switch').prop("checked")) {
            $.ajax({
                url: "https://c64aas.com/api/program",
                contentType: my_content_type,
                headers: my_headers,
                type: 'GET',
                success: function (response) {
                    output = JSON.stringify(response)
                    output.replace(/\r\n/g , "<br>");
                    $('#in_form').val(output)
                }
            });
	} else {
            $.ajax({
                url: "https://c64aas.com/api/program",
                contentType: my_content_type,
                headers: my_headers,
                type: 'GET',
                success: function (response) {
                    output = response
                    output.replace(/\r\n/g , "<br>");
                    $('#in_form').val(output)
                }
            });
	}
    };

    $('#run_btn').click(function () {
        var data = {}
        var body = ""
        var my_content_type = "text/plain"
        var my_headers = {
                          Accept: "text/plain; charset=utf-8",
                          "Content-Type": "text/plain; charset=utf-8"
                          }
        if ($('#json_switch').prop("checked")) {
	    try {
                data = JSON.parse($('#in_form').val())
	    } catch (e) {
                console.log("error: "+e);
            };
            body = JSON.stringify(data)
            my_content_type = "application/json"
            my_headers = {}
        } else {
            data = $('#in_form').val()
            body = data
        }
        console.log(body)
        $.ajax({
            url: "https://c64aas.com/api/program",
            contentType: my_content_type,
            data: body,
            type: 'POST',
            success: function (response1) {
                console.log("POST was successful!")
                $.ajax({
                    url: "https://c64aas.com/api/run",
		    contentType: my_content_type,
                    headers: my_headers,
                    type: 'GET',
                    success: function (response2) {
                        //console.log(response2)
                        //output = JSON.stringify(response2)
                        output = response2
                        output.replace(/\r\n/g , "<br>");
                        $('#out_form').val(output)
                    }
                });
            },
            error: function (xhr, ajaxOptions, thrownError) {
                alert(xhr.status + ' ' + thrownError);
            }		
        });
    })
});
