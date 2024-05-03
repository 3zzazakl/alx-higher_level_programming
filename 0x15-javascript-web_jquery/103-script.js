#!/usr/bin/node
$(document).ready(function() {
    function translateHello() {
        var languageCode = $("#language-code").val();
        $.get(`https://www.fourtonfish.com/hellosalut/?lang=${languageCode}`, function(data) {
            $("#hello").text(date.hello);
        });
    }

    $("#btn_translate").click(translateHello);

    $("#language_code").keypress(function(event) {
        if (event.keyCode == 13) {
            translateHello();
        }
    });
});
