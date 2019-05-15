// Listener that tells the user whether the username they have typed in as available for use
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


// Listener that displays each of the friends whose name contains the substring
$(document).ready(function () {
    $('#username_search').keyup(function () {
        var data = $("#username_search").serialize()   // capture all the data in the form in the variable data
        $.ajax({
            method: "POST",   // we are using a post request here, but this could also be done with a get
            url: "/username_search",
            data: data
        })
            .done(function (res) {
                $('#friends').html(res);
            })
    })
})


