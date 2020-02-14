$.getJSON( "https://swapi.co/api/films/?format=json", function(data) {
    for (let con = 0; con < data.results.length ; con ++) {
        console.log(data.results[con].title);
        $('ul#list_movies').append($("<li></li>").text(data.results[con].title));
    }
});