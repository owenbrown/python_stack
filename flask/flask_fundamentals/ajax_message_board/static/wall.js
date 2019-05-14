$(document).ready(function () {
    $('#email').keyup(function () {
        var data = $("#email").serialize()   // capture all the data in the form in the variable data
        $.ajax({
            method: "POST",   // we are using a post request here, but this could also be done with a get
            url: "/username",
            data: data
        })
            .done(function (res) {
                $('#emailMsg').html(res);
                if (res == "Email is free") {
                    $('#emailMsg').css('color', 'green');
                } else {
                    $('#emailMsg').css('color', 'red');
                    console.log("no");
                    console.log("george");
                }


            })
    })
})