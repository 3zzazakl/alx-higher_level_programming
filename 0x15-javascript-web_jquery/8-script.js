#!/usr/bin/node
$(document).ready(function () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
    data.results.forEach(function (movie) {
      $('#list_movies').append('<li>' + movie.title + '</li>');
    });
  });
});
