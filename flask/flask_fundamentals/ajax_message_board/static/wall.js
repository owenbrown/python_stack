$(document).ready(function () {
    $('#username').keyup(function () {
        var data = $("#username").serialize()   // capture all the data in the form in the variable data
        $.ajax({
            method: "POST",   // we are using a post request here, but this could also be done with a get
            url: "/username",
            data: data
        })
            .done(function (res) {
                $('#usernameMsg').html(res);
                if (res == "Username available") {
                    $('#usernameMsg').css('color', 'green');
                } else {
                    $('#usernameMsg').css('color', 'red');
                }


            })
    })
})

