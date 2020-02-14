$('DIV#toggle_header').click(function() {
    $('header').toggleClass("green", "red");
    $('header').toggleClass("red", "green"); 
});